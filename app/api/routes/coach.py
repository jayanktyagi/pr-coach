from fastapi import APIRouter
from app.schemas.coach import CoachRequest
from app.graphs.coach_graph import coach_graph
from app.graphs.state import CoachState

router = APIRouter()

@router.post("/coach")
def coach(req: CoachRequest):
    initial_state: CoachState = {
        "question": req.question,
        "exercise_sets": [],
        "metrics": {},
        "response": ""
    }

    result = coach_graph.invoke(initial_state)
    return {"response": result["response"]}