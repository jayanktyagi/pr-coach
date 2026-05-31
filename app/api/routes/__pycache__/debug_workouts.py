from fastapi import APIRouter
router = APIRouter()
from app.db.session import SessionLocal
from app.db.models import ExerciseSet

@router.get("/debug/workouts")
def debug_workouts():
    rows = SessionLocal().query(ExerciseSet).limit(10).all()
    return rows