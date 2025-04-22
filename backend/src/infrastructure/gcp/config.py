from google.cloud import aiplatform
from src.domain.job import Job

# Initialize AI Platform
aiplatform.init(
    project="YOUR_GCP_PROJECT_ID",
    location="us-central1"
)

def submit_training_job(job_data: dict):
    job = aiplatform.CustomJob(
        display_name=f"lora-training-{job_data['id']}",
        worker_pool_specs=[{
            "machine_spec": {"machine_type": "n1-standard-8", "accelerator_type": "NVIDIA_TESLA_T4", "accelerator_count": 1},
            "replica_count": 1,
            "python_package_spec": {
                "executor_image_uri": "gcr.io/cloud-aiplatform/training/tensorflow:latest",
                "package_uris": ["gs://your-bucket/ai-toolkit-package.tar.gz"],
                "python_module": "aitoolkit.train",
                "args": [f"--config={job_data}"]
            }
        }]
    )
    job.run(sync=False)