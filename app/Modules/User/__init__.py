from flask import Blueprint

user = Blueprint('users', __name__, template_folder='templates/users')

from . import Controller
