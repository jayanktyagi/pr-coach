from typing import TypedDict, List, Dict

class CoachState(TypedDict):
    question: str
    exercise_sets: List[dict]
    metrics: Dict
    insights: str
    response: str