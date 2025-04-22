# Flux LoRA Training App

A full-stack application to configure, launch, and monitor Flux LoRA training jobs with customizable settings, using Ostris AI-Toolkit and GCP for scalable GPU training.

## Project Structure

```
flux-lora-app/
├── .gitignore
├── README.md
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── src/
│   │   ├── domain/
│   │   │   └── job.py
│   │   ├── application/
│   │   │   └── job_service.py
│   │   ├── infrastructure/
│   │   │   ├── aitoolkit_adapter.py
│   │   │   └── gcp/config.py
│   │   └── presentation/
│   │       └── job_controller.py
│   └── app.py
├── frontend/
│   ├── package.json
│   ├── tsconfig.json
│   ├── tailwind.config.js
│   └── src/
│       ├── App.tsx
│       ├── components/
│       │   ├── JobForm.tsx
│       │   └── JobList.tsx
│       └── services/
│           └── api.ts
└── terraform/
    └── main.tf
```

## Features

- **Backend**: FastAPI with clean architecture (domain, application, infrastructure, presentation).
- **Frontend**: React + TypeScript + Tailwind CSS; reactive form for job creation and live job list.
- **Training Adapter**: Integrates Ostris AI-Toolkit CLI or GCP Vertex AI CustomJob for LoRA training.
- **Infrastructure**: Terraform scripts to provision GCP compute instances in Europe-West1 (Belgium) region for parallel training.

## Prerequisites

### Local
- Python 3.10+
- Node.js & npm
- Docker (optional for container testing)

### Cloud
- GCP project with Vertex AI & Compute Engine permissions
- Google Cloud Storage bucket
- `gcloud` CLI authenticated
- Terraform CLI installed

## Setup Guide

### 1. Clone Repository
```bash
git clone git@github.com:WardGovaert/flux-lora-app.git
cd flux-lora-app
```

### 2. Backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload
```
API endpoint: `http://localhost:8000/jobs`

### 3. Frontend
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
npm run dev
```
Dev server: `http://localhost:3000`

### 4. Git & GitHub
Ensure `.gitignore` is present to exclude `node_modules/`, `__pycache__/`, `.terraform/`, and sensitive files.
```bash
git add .
git commit -m "Initial project commit"
git remote add origin git@github.com:<your-username>/flux-lora-app.git
git push -u origin main
```

### 5. GCP Deployment (Terraform)
1. Edit `terraform/main.tf`, set `project = "YOUR_GCP_PROJECT_ID"`, region/zone.
2. Initialize & apply:
```bash
cd terraform
terraform init
terraform apply
```
3. SSH into the instance and verify startup script:
```bash
gcloud compute ssh lora-trainer --zone europe-west1-b
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a Pull Request with details

## License

MIT License. See `LICENSE` file.

---

## .gitignore

```gitignore
# Node.js
node_modules/
# Python
__pycache__/
*.pyc
# Terraform
.terraform/
*.tfstate
# Environment
.env
# Logs
*.log
# macOS
.DS_Store
```

