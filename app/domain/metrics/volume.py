def weekly_volume(exercise_sets):
    """
    Calculate total training volume (weight_kg * reps)
    for a list of ExerciseSet records.

    Ignores sets with missing weight or reps.
    """
    total_volume = 0.0
    for s in exercise_sets:
        weight = getattr(s, "weight", None)
        reps = getattr(s, "reps", None)

        if weight is None or reps is None:
            continue

        try:
            total_volume += float(weight) * int(reps)
        except (TypeError, ValueError):
            # Handles NaN or invalid data
            continue

    return round(total_volume, 2)

from collections import defaultdict

def weekly_volume_by_exercise(exercise_sets):
    volume = defaultdict(float)

    for s in exercise_sets:
        name = s.get("exercise")
        weight = s.get("weight")
        reps = s.get("reps")

        if name is None or weight is None or reps is None:
            continue

        try:
            volume[name] += float(weight) * int(reps)
        except (TypeError, ValueError):
            continue

    return dict(volume)