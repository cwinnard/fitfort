from flask import Flask, redirect, url_for
from flask_cors import CORS
from flask_login import login_manager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'isyfms'

#Alow local hits
#TODO review this
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hero:hero@localhost/fit'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#Configure login
loginManager = login_manager.LoginManager()
from psql.schema.master import User

@loginManager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
    
loginManager.init_app(app)

from fitflask.master.controller import masterBP
app.register_blueprint(masterBP)
from fitflask.summary.controller import summaryBP
app.register_blueprint(summaryBP)
from fitflask.workout.controller import workoutBP
app.register_blueprint(workoutBP)

@app.route('/')
def index():
    return 'Hello World!'