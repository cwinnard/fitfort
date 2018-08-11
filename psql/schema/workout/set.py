from fitflask import db


class Set(db.Model):
    """Represents a set within an exercise"""

    __table_args__ = {'schema': 'workout'}
    __tablename__ = 'set'

    id = db.Column(db.Integer, primary_key=True)
    reps = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    id_exercise = db.Column(db.Integer, db.ForeignKey('workout.exercise.id'), nullable=False)