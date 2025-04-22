import subprocess
from src.domain.job import Job

class AiToolkitAdapter:
    """
    Adapter to call Ostris AI-Toolkit CLI for LoRA training.
    """
    def train(self, job: Job, data_path: str):
        cmd = [
            "ai-toolkit", "train",
            "--model", "FLUX.1-dev",
            f"--steps", str(job.epochs),
            f"--learning-rate", str(job.learning_rate),
            f"--caption-mode", job.caption_method,
            f"--data", data_path,
        ]
        subprocess.Popen(cmd)