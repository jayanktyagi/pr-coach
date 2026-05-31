from app.db.session import SessionLocal
from app.db.models import ExerciseSet, Exercise, Workout

def load_history_node(state):
    session = SessionLocal()
    try:
        rows = (
            session.query(ExerciseSet)
            .join(Exercise)
            .join(Workout)
            .all()
        )

        exercise_sets = [
            {
                "exercise": r.exercise.name,
                "weight": r.weight_kg,
                "reps": r.reps,
                "rpe": r.rpe,
                "set_type": r.set_type,
                "date": r.exercise.workout.start_time.isoformat()
                if r.exercise.workout.start_time else None,
            }
            for r in rows
        ]

        return {
            **state,
            "exercise_sets": exercise_sets
        }

    finally:
        session.close()