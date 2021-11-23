from flask import Blueprint, render_template, request, url_for, session, redirect, flash
from db_connect import db
from models.models import *
from werkzeug.security import generate_password_hash, check_password_hash
from .check import password_match_string, password_match_int, password_match_special

from .forms import RegisterForm, LoginForm


bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if session.get('user_id'):
        return redirect(url_for("main.home"))
    
    form = RegisterForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            nickname = form.nickname.data
            telephone = form.telephone.data
            # 비밀번호 확인 
            # 비밀번호가 10자리 이상이면 영문 숫자 특사문자 중 2개 이상
            # if not any(isinstance(char, str) for char in password):
            #     flash('비밀번호는 영어 대소문자가 포함되어야합니다.')
            #     return redirect(url_for('user.register', form = form))
            # if not any(char.isdigit() for char in password):
            #     flash('비밀번호는 숫자가 포함되어야합니다.')
            #     return redirect(url_for('user.register', form = form))
            # special_char = '`~!@#$%^&*()_+|\\}{[]":;\'?><,./'
            # if not any(char in special_char for char in password):
            #     flash('비밀번호는 특수문자가 포함되어야합니다.')
            #     return redirect(url_for('user.register', form=form))
            if len(password) >= 10:
                count = 0
                if password_match_string(password) is True:
                    count+=1
                if password_match_int(password) is True:
                    count+=1
                if password_match_special(password) is True:
                    count+=1
                
                if count<2:
                    flash('비밀번호가 10자리 이상이면 특수문자, 영어 대소문자, 숫자 중 2개 이상의 조합이 필요합니다.')
                    return redirect(url_for('user.register', form=form)) 
            
            if 8 <= len(password) < 10:
                count = 0
                if password_match_string(password) is True:
                    count+=1
                if password_match_int(password) is True:
                    count+=1
                if password_match_special(password) is True:
                    count+=1
                
                if count != 3:
                    flash('비밀번호가 8자리 이상, 10자리 이하이면 특수문자, 영어 대소문자, 숫자 모두를 포함하여야 합니다.')
                    return redirect(url_for('user.register', form=form))
                    
            if UserInfo.query.filter(UserInfo.user_id == email).first() is not None:
                flash('이미 사용 중인 아이디(이메일) 입니다.')
                return redirect(url_for('user.register', form=form))
            
            hash_password = generate_password_hash(password)
            
            user = UserInfo(user_id = email, user_pw = hash_password, user_number = telephone, user_nickname = nickname)
            db.session.add(user)
            db.session.commit()
            flash('회원가입이 성공적으로 완료 되었습니다.')
            return redirect(url_for('main.home'))
        else:
            for message in form.errors.values():
                flash(str(message[-1]))
    
    return render_template('register.html', form = form)
    
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('user_id'):
        return redirect(url_for('main.home'))

    form = LoginForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            
            user = UserInfo.query.filter(UserInfo.user_id == email).first()
        
            if user is not None and not check_password_hash(user.user_pw, password):
                flash('비밀번호가 틀렸습니다.')
                return redirect(url_for('user.login', form = form))
            else:
                session['user_id'] = email
                session['nickname'] = user.user_nickname
                flash(f"{user.user_nickname}님, 환영합니다.")
                return redirect(url_for('main.home'))
        else:
            for message in form.errors.values():
                flash(str(message[-1]))
    
    return render_template('login.html', form = form)
    
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.home'))