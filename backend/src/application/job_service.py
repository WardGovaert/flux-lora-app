from src.domain.job import Job
from src.infrastructure.aitoolkit_adapter import AiToolkitAdapter
from src.infrastructure.gcp.config import submit_training_job

class JobService:
    def __init__(self, adapter: AiToolkitAdapter):
        self.adapter = adapter

    def create_job(self, epochs: int, lr: float, caption_method: str) -> Job:
        job = Job.create(epochs, lr, caption_method)
        # submit using AI Toolkit
        submit_training_job(job.dict())
        return job

    def list_jobs(self) -> list[Job]:
        # stub: fetch from persistent store
        return []