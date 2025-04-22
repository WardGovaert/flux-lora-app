from fastapi import FastAPI
from src.presentation.job_controller import router as job_router

app = FastAPI()
app.include_router(job_router, prefix="/jobs", tags=["jobs"])