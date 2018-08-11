from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user

from fitflask import db
#from .login_facilitator import LoginFacilitator
from psql.schema.master import User

loginBP = Blueprint('login', __name__, url_prefix='/login')

@loginBP.route('/')
def welcome():
    return 'Hello Login!'

@loginBP.route('/login-user')
def log_user_in():
    userName = request.args.get('username')
    user = User.query.filter_by(user_name=userName).first()
    #LoginFacilitator().log_user_in(user)
    return 200

@loginBP.route('/create-user')
def create_user():
    user_name = request.args.get('username')
    name_first = request.args.get('firstname')
    name_last = request.args.get('lastname')
    email = request.args.get('email')
    password = request.args.get('password')

    newUser = User()
    newUser.user_name = user_name
    newUser.name_first = name_first
    newUser.name_last = name_last
    newUser.email = email
    newUser.password = password

    db.session.add(newUser)
    db.session.commit()

    #LoginFacilitator().log_user_in(newUser)
    return redirect(url_for('dashboard.dashboard'))
