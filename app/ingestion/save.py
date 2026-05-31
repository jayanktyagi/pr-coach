from app.db.models import Workout, Exercise, ExerciseSet

def save_records(session, records):
    for r in records:
        workout = (
            session.query(Workout)
            .filter_by(start_time=r["start_time"])
            .first()
        )

        if not workout:
            workout = Workout(
                title=r["title"],
                start_time=r["start_time"],
                end_time=r["end_time"],
                description=r["description"]
            )
            session.add(workout)
            session.flush()

        exercise = (
            session.query(Exercise)
            .filter_by(
                workout_id=workout.id,
                name=r["exercise_title"],
                superset_id=r["superset_id"]
            )
            .first()
        )

        if not exercise:
            exercise = Exercise(
                workout_id=workout.id,
                name=r["exercise_title"],
                superset_id=r["superset_id"],
                notes=r["exercise_notes"]
            )
            session.add(exercise)
            session.flush()

        exists = (
            session.query(ExerciseSet)
            .filter_by(
                exercise_id=exercise.id,
                set_index=r["set_index"]
            )
            .first()
        )

        if not exists:
            session.add(ExerciseSet(
                exercise_id=exercise.id,
                set_index=r["set_index"],
                set_type=r["set_type"],
                weight_kg=r["weight_kg"],
                reps=r["reps"],
                distance_km=r["distance_km"],
                duration_seconds=r["duration_seconds"],
                rpe=r["rpe"]
            ))

    session.commit()