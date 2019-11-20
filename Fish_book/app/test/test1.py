# Blueprint视图函数

from . import test
from flask import render_template,flash


@test.route('/test')
def search():
    data = {
        'name': 'zou',
        'age': 24
    }
    flash('hello,zou')
    return render_template('test.html', data=data)
