from flask import Flask, redirect, url_for
from flask_login import login_manager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hero:hero@localhost/fit'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import psql

@app.route('/')
def index():
    return 'Hello World!'