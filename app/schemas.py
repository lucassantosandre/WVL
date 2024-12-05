from typing import List, Optional
from pydantic import BaseModel

class SetData(BaseModel):
    reps: int
    weight: float

class ExerciseData(BaseModel):
    exercise_name: str
    sets: List[SetData]
    max_weight: Optional[float] = None  # Peso máximo para progressão
    reps_at_max: Optional[int] = None  # Reps no peso máximo

class WorkoutRequest(BaseModel):
    exercises: List[ExerciseData]

class WorkoutResponse(BaseModel):
    exercise_volumes: dict
    total_volume: float
    suggestions: str
    progression_details: dict
