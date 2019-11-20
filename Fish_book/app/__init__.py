from flask import Flask
from app.models.base import db
from flask_login import LoginManager
from flask_mail import Mail

loginManager = LoginManager()
mail = Mail()


def create_app():
    # __name__ 规定了程序根目录
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    loginManager.init_app(app)
    loginManager.login_view = 'web.login'
    loginManager.login_message = '请先登录或注册'
    mail.init_app(app)
    db.create_all(app=app)
    return app


# current_app -> (LocalStack.top = AppContext top.app)
# 传递核心 app
def register_blueprint(app):
    from app.web.book import web
    from app.test import test
    app.register_blueprint(web)
    app.register_blueprint(test)

