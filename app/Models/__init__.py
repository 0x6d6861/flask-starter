from app import db, login_manager
from app.Models.User import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))