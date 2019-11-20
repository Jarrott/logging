from flask import Blueprint

test = Blueprint('test', __name__, template_folder='templates')

from app.test import test1