class RecordLift:

    def __init__(self, exercise_name=None, weight=None, date=None):
        self.exercise_name = exercise_name
        self.weight = weight
        self.date = date

    def serialize(self):
        return {
            'exercise_name': self.exercise_name, 
            'weight': self.weight,
            'date': self.date
        }