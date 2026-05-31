from fastapi import FastAPI
from app.api.routes.ingest import router as ingest_router
from app.api.routes.coach import router as coach_router

app = FastAPI()

app.include_router(ingest_router)
app.include_router(coach_router)