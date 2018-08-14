from flask import Blueprint, jsonify, request
from flask_login import current_user

from fitflask import db
from psql.schema.workout import Exercise, Set, Workout
from .summarizer import Summarizer

summaryBP = Blueprint('summary', __name__, url_prefix='/summary')

@summaryBP.route('/')
def welcome():
    return 'Hello Summary!'

@summaryBP.route('/workouts', methods=['GET'])
def get_all_workouts():
    workouts = Workout.query.filter_by(id_user=current_user.id).all()
    return jsonify(workouts=[workout.serialize() for workout in workouts])

@summaryBP.route('/records', methods=['GET'])
def get_record_lifts():
    summarizer = Summarizer()
    recordLifts = summarizer.get_record_lifts(current_user)

    return jsonify(recordLifts=[recordLift.serialize() for recordLift in recordLifts])