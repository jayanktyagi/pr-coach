from app.db.session import SessionLocal
from app.db.models import ExerciseSet, Exercise, Workout

def clear_db():
    session = SessionLocal()

    # Order matters because of foreign keys
    session.query(ExerciseSet).delete()
    session.query(Exercise).delete()
    session.query(Workout).delete()

    session.commit()
    session.close()

    print("✅ Database cleared successfully")

if __name__ == "__main__":
    clear_db()