from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from flask_login import current_user

from fitflask import db
from .login_facilitator import LoginFacilitator
from psql.schema.master import User

loginBP = Blueprint('login', __name__, url_prefix='/login')

@loginBP.route('/')
def welcome():
    return 'Hello Login!'

@loginBP.route('/login-user', methods=['POST'])
def log_user_in():
    email = request.form.get('email')
    user = User.query.filter_by(email=email).first()
    LoginFacilitator().log_user_in(user)
    return jsonify(current_user.serialize())

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

    LoginFacilitator().log_user_in(newUser)
    return redirect(url_for('dashboard.dashboard'))
