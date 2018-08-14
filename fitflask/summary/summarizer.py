from .models import RecordLift
from psql.schema.workout import Exercise, Set, Workout


class Summarizer:

    def get_record_lifts(self, user):
        exercises = Exercise.query.join(Workout).filter(Workout.id_user == user.id).all()
        recordLifts = self._build_record_lifts(exercises)
        return recordLifts

    def _build_record_lifts(self, exercises):
        recordLifts = []
        for exercise in exercises:
            if any(recordLift.exercise_name == exercise.name for recordLift in recordLifts):
                if exercise.max_weight > recordLift.weight:
                    recordLifts[exercise.name].weight = exercise.max_weight
            else:
                recordLift = RecordLift(exercise_name=exercise.name, 
                                        weight=exercise.max_weight,
                                        date=exercise.workout.start)
                recordLifts.append(recordLift)

        return recordLifts

        

