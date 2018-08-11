from fitflask import db


class Exercise(db.Model):
    """Represents an exercise within a workout"""

    __table_args__ = {'schema': 'workout'}
    __tablename__ = 'exercise'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    id_workout = db.Column(db.Integer, db.ForeignKey('workout.workout.id'), nullable=False)

    sets = db.relationship('Set', backref='exercise', lazy='joined')

    def serialize(self):
        return {
            'name': self.name
        }