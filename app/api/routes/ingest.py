from fastapi import APIRouter, UploadFile, File, HTTPException
from app.ingestion.hevy_csv import parse_hevy_csv
from app.ingestion.save import save_records
from app.db.session import SessionLocal

router = APIRouter()
@router.post("/sync/hevy")
async def ingest_hevy(file: UploadFile = File(...)):
    session = None

    try:
        records = parse_hevy_csv(file)

        session = SessionLocal()
        save_records(session, records)

        return {
            "status": "success",
            "records_ingested": len(records)
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    finally:
        if session:
            session.close()