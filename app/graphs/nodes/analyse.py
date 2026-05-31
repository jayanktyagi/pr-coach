from app.domain.metrics.volume import weekly_volume, weekly_volume_by_exercise, weekly_volume_by_exercise

def analyze_node(state):
    metrics = {
    "weekly_volume_total": weekly_volume(state["exercise_sets"]),
    "weekly_volume_by_exercise": weekly_volume_by_exercise(state["exercise_sets"])
    }
    return {
        **state,
        "metrics": metrics
    }