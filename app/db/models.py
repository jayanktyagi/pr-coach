from sqlalchemy import (
    Column, Integer, String, DateTime, Float, ForeignKey
)
from sqlalchemy.orm import relationship
from app.db.session import Base


class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    start_time = Column(DateTime, unique=True, index=True)
    end_time = Column(DateTime)
    description = Column(String(255))

    exercises = relationship("Exercise", back_populates="workout")


class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True)
    workout_id = Column(Integer, ForeignKey("workouts.id"))
    name = Column(String(100))
    superset_id = Column(String(50), nullable=True)
    notes = Column(String(255), nullable=True)

    workout = relationship("Workout", back_populates="exercises")
    sets = relationship("ExerciseSet", back_populates="exercise")


class ExerciseSet(Base):
    __tablename__ = "exercise_sets"

    id = Column(Integer, primary_key=True)
    exercise_id = Column(Integer, ForeignKey("exercises.id"))
    set_index = Column(Integer)
    set_type = Column(String(20))
    weight_kg = Column(Float)
    reps = Column(Integer)
    distance_km = Column(Float)
    duration_seconds = Column(Integer)
    rpe = Column(Float)

    exercise = relationship("Exercise", back_populates="sets")