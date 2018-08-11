from datetime import datetime
from time import strftime

from fitflask import db
from sqlalchemy.sql import func

from psql.schema.master import User


class Workout(db.Model):
    """Represents a workout"""

    __table_args__ = {'schema': 'workout'}
    __tablename__ = 'workout'

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    ts_start = db.Column(db.DateTime(), nullable=False, default=datetime.now(), server_default=func.now())
    ts_finish = db.Column(db.DateTime())

    exercises = db.relationship('Exercise', backref='workout', lazy='joined')

    @property
    def start(self):
        return self.ts_start.strftime('%b %d %Y')

    @property
    def finish(self):
        return self.ts_finish.strftime('%b %d %Y') if self.ts_finish else ''

    def serialize(self):
        return {
            'start': self.start,
            'finish': self.finish
        }