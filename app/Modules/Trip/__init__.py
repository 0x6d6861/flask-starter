from flask import Blueprint

trip = Blueprint('trips', __name__, template_folder='templates/main')

from . import Controller
