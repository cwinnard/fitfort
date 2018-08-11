from fitflask import db


class User(db.Model):
    """Represents a person"""

    __table_args__ = {'schema': 'master'}
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(128), nullable=False)
    name_first = db.Column(db.String(128), nullable=False)
    name_last = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    authenticated = db.Column(db.Boolean, default=False)

    workouts = db.relationship('Workout', backref='user', lazy='joined')

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

    def serialize(self):
        return {
            'name': '{} {}'.format(self.name_first, self.name_last), 
            'username': self.user_name,
            'email': self.email
        }