from flask import Blueprint, render_template, request, url_for, session, redirect, flash, g
from db_connect import db
from models.models import *
from werkzeug.security import generate_password_hash, check_password_hash


bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        id = request.form['user_id']
        pw = generate_password_hash(request.form['password'])
        nickname = request.form['user_nickname']
        telephone = request.form['telephone']
        
        user = UserInfo.query.filter(UserInfo.user_id == id).first()
        if not user:
            user = UserInfo(id, pw, telephone, nickname)
            db.session.add(user)
            db.session.commit()
            flash('elice 도서관에 오신걸 환영합니다!')
            return redirect(url_for('user.login'))
        else:
            flash('이미 존재하는 아이디입니다.')
            return redirect(url_for('user.register'))
    
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user_id = request.form['user_id']
        user_pw = request.form['password']

        user = UserInfo.query.filter(UserInfo.user_id == user_id).first()
        
        if not user:
            flash('존재하지 않는 아이디입니다.')
            return redirect(url_for('user.login'))
        elif not check_password_hash(user.user_pw, user_pw):
            flash('비밀번호가 틀렸습니다.')
            return redirect(url_for('user.login'))
        else:
            session.clear()
            session['user_id'] = user_id
            session['nickname'] = user.user_nickname
            flash(f"{user.user_nickname}님, 환영합니다.")
            return redirect(url_for('main.home'))

@bp.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect(url_for('main.home'))    