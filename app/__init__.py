from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# db variable initialization
db = SQLAlchemy()

from flask_login import LoginManager
login_manager = LoginManager()



# local imports
from config import app_config

from .Modules.User import user as userModule




def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    # db.create_all()
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    # MODULES
    app.register_blueprint(userModule, url_prefix='/users')

    return app
