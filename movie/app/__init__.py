from flask import Flask
from app.models.base import db


def create_app():

    app = Flask(__name__)
    app.debug = True

    from app.home import home as home_blueprint
    from app.admin import admin as admin_blueprint

    app.register_blueprint(home_blueprint)
    app.register_blueprint(admin_blueprint, url_prefix="/admin")
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@127.0.0.1:3306/movie"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.init_app(app)
    db.create_all(app=app)
    return app
