from wtforms import Form, StringField, IntegerField, PasswordField
from wtforms.validators import Length, NumberRange, DataRequired, Email, ValidationError, EqualTo

from app.models.user import User


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='邮箱格式不规范')])
    password = PasswordField(validators=[DataRequired(message='密码不能为空'), Length(6, 32)])
    nickname = StringField(validators=[DataRequired(), Length(2, 10, message='昵称至少需要两个字符，最多10个字符')])

    def vaildate_email(self, field):
        User.query.filter_by(email=field.data).first()
        raise ValidationError('该邮箱已被注册')

    def vaildate_nickname(self, field):
        User.query.filter_by(nickname=field.data).first()
        raise ValidationError('昵称已存在')


class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='邮箱格式不规范')])
    password = PasswordField(validators=[DataRequired(message='密码不能为空'), Length(6, 32)])


class EmailForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='邮箱格式不规范')])


class ResetPasswordForm(Form):
    password1 = PasswordField(validators=[
        DataRequired(),
        Length(6, 32, message='密码长度至少需要在6到32个字符之间'),
        EqualTo('password2', message='两次输入的密码不相同')
    ])
    password2 = PasswordField(validators=[
        DataRequired(), Length(6, 32)])
