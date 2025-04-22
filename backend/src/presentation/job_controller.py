from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.application.job_service import JobService
from src.infrastructure.aitoolkit_adapter import AiToolkitAdapter

router = APIRouter()
service = JobService(AiToolkitAdapter())

class CreateJobRequest(BaseModel):
    epochs: int
    learning_rate: float
    caption_method: str
    data_path: str

@router.post("/", response_model=dict)
async def create_job(req: CreateJobRequest):
    job = service.create_job(req.epochs, req.learning_rate, req.caption_method)
    return job.dict()

@router.get("/", response_model=list[dict])
async def list_jobs():
    return [j.dict() for j in service.list_jobs()]