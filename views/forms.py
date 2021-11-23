from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired, EqualTo

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[
        DataRequired("이메일을 입력해주세요."),
        validators.Email("올바른 형식의 이메일을 입력해주세요.")])
    
    password = PasswordField('password', validators=[
        DataRequired("비밀번호를 입력해주세요."),
        EqualTo('re_password', "비밀번호는 동일해야 합니다."),
        validators.Length(min=8, message="비밀번호는 최소 8자리 이상, 영어 대소문자, 숫자, 특수문자만 가능합니다."),
        ])
    
    re_password = PasswordField('re_password', validators=[DataRequired("비밀번호를 확인해주세요.")])
    
    nickname = StringField('nickname', validators=[
        DataRequired("닉네임을 입력해주세요."),
        validators.Regexp(regex='[가-힣a-zA-Z]+', message="닉네임은 한글과 영문만 사용 가능합니다.") 
        ])
    
    telephone = StringField('telephone', validators=[
        DataRequired("전화번호를 입력해주세요"),
        validators.Regexp(regex='[0-9]+', message="전화번호는 숫자만 사용 가능합니다.")])


class LoginForm(FlaskForm):
    email = StringField('email', validators=[
        DataRequired("이메일을 입력해주세요."),
        validators.Email("올바른 형식의 이메일을 입력해주세요.")
    ])
    
    password = PasswordField('password', validators=[
        DataRequired("비밀번호를 입력해주세요.")
    ])