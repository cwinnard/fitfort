from flask import Blueprint, jsonify, request
from flask_login import current_user

from fitflask import db
from psql.schema.workout import Exercise, Set, Workout

workoutBP = Blueprint('workout', __name__, url_prefix='/workout')

@workoutBP.route('/')
def welcome():
    return 'Hello Workout!'

@workoutBP.route('/start', methods=['POST'])
def start():
    workout = Workout()
    workout.id_user = current_user.id
    db.session.add(workout)
    db.session.commit()
    return jsonify(workout.serialize())

@workoutBP.route('/exercise/new', methods=['POST'])
def new_exercise():
    name = request.form.get('name')
    workoutId = request.form.get('workoutId')
    exercise = Exercise()
    exercise.name = name
    exercise.id_workout = workoutId
    db.session.add(exercise)
    db.session.commit()
    return jsonify(exercise.serialize())

