import pandas as pd
from datetime import datetime

def parse_hevy_datetime(value: str | None):
    if not value or not isinstance(value, str):
        return None

    return datetime.strptime(value, "%d %b %Y, %H:%M")

def parse_hevy_csv(file) -> list[dict]:
    df = pd.read_csv(file.file)

    records = []
    for _, row in df.iterrows():
        records.append({
            "title": row["title"],
            "start_time": parse_hevy_datetime(row.get("start_time")),
            "end_time": parse_hevy_datetime(row.get("end_time")),
            "description": row.get("description"),
            "exercise_title": row["exercise_title"],
            "superset_id": row.get("superset_id"),
            "exercise_notes": row.get("exercise_notes"),
            "set_index": int(row["set_index"]),
            "set_type": row["set_type"],
            "weight_kg": row.get("weight_kg"),
            "reps": row.get("reps"),
            "distance_km": row.get("distance_km"),
            "duration_seconds": row.get("duration_seconds"),
            "rpe": row.get("rpe"),
        })
        records = [
            {k: (None if v != v else v) for k, v in r.items()}
            for r in records
        ]
    return records