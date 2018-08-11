from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from flask_login import current_user

from fitflask import db
from .login_facilitator import LoginFacilitator
from psql.schema.master import User

masterBP = Blueprint('master', __name__, url_prefix='/master')

@masterBP.route('/')
def welcome():
    return 'Hello Master!'

@masterBP.route('/user/login', methods=['POST'])
def log_user_in():
    email = request.form.get('email')
    user = User.query.filter_by(email=email).first()
    LoginFacilitator().log_user_in(user)
    return jsonify(current_user.serialize())

@masterBP.route('/user/create', methods=['POST'])
def create_user():
    user_name = request.form.get('username')
    name_first = request.form.get('firstname')
    name_last = request.form.get('lastname')
    email = request.form.get('email')
    password = request.form.get('password')

    newUser = User()
    newUser.user_name = user_name
    newUser.name_first = name_first
    newUser.name_last = name_last
    newUser.email = email
    newUser.password = password

    db.session.add(newUser)
    db.session.commit()

    LoginFacilitator().log_user_in(newUser)
    return jsonify(current_user.serialize())
