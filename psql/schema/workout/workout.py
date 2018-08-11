from time import strftime

from fitflask import db

from psql.schema.master import User


class Workout(db.Model):
    """Represents a workout"""

    __table_args__ = {'schema': 'workout'}
    __tablename__ = 'workout'

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    ts_start = db.Column(db.DateTime(), nullable=False)
    ts_finish = db.Column(db.DateTime())

    @property
    def start(self):
        return self.ts_start.strftime('%b %d %Y')

    @property
    def finish(self):
        return self.ts_end.strftime('%b %d %Y')

    def serialize(self):
        return {
            'name': self.name, 
            'start': self.start,
            'finish': self.finish
        }