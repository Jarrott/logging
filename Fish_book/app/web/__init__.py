from flask import Blueprint, render_template

# 规定蓝图的templates template_folder=
web = Blueprint('web', __name__)

# 导入视图函数
from app.web import book
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
from app.web import auth


@web.app_errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404
