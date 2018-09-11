from app import db
from . import user

from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, logout_user, login_user


from app.Models.User import User as UserModel
from app.Modules.User.forms import LoginForm, RegistrationForm

@login_required
@user.route('/')
def index():
    print(UserModel.query.filter_by(email='agape@live.fr').first())
    return "Hello Users"


@user.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form, csrf_enabled=True)
    if request.method == 'POST':
        # check whether employee exists in the database and whether
        # the password entered matches the password in the database
        user = UserModel.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(
                form.password.data):
            # log employee in
            login_user(user)

            # login_user(user, remember=False, duration=None, force=False, fresh=True)

            # redirect to the dashboard page after login
            return redirect(url_for('trips.index'))

        # when login details are incorrect
        else:
            flash('Invalid email or password.', 'error')

    # load login template
    return render_template('auth/login.html', form=form, title='Login')


@user.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add an employee to the database through the registration form
    """
    form = RegistrationForm(request.form, csrf_enabled=True)
    if request.method == 'POST' and form.validate():
        user_new = UserModel(email=form.email.data,
                        name=form.name.data,
                        password=form.password.data)
        # add employee to the database
        db.session.add(user_new)
        db.session.commit()
        flash('You have successfully registered! You may now login.')

        # redirect to the login page
        return redirect(url_for('users.login'))

    # load registration template
    return render_template('auth/register.html', form=form, title='Register')


@user.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an employee out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('users.login'))
