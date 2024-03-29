from wtforms import Form, StringField
from wtforms.validators import DataRequired, Length, Regexp


class DriftForm(Form):
    recipient_name = StringField(
        '收件人姓名', validators=[DataRequired(), Length(min=2, max=20,
                                                    message='收件人姓名长度必须在2到20个字符之间')])
    mobile = StringField('手机号', validators=[DataRequired(),
                                            Regexp('^1[0-9]{10}$', 0, '请输入正确的手机号')])
    message = StringField('留言')
    address = StringField(
        '邮寄地址', validators=[DataRequired(),
                            Length(min=10, max=70, message='地址还不到10个字吗？尽量写详细一些吧')])