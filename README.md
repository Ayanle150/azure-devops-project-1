# Project 1 – Cloud-Native Application on Azure

**Docker · GitHub Actions · Azure · CI/CD**

This project demonstrates an end-to-end DevOps workflow, from local development to automated testing, containerization, and deployment readiness in Azure.
The focus is on **clean structure, automation, secure handling of credentials, and real-world cloud constraints**.

---

## Project Overview

The goal of this project is to build and deploy a simple cloud-native application using modern DevOps principles.

It covers the full lifecycle:
- Local development
- Containerization with Docker
- Continuous Integration (CI)
- Publishing artifacts to Azure Container Registry
- Deployment using Azure Container Apps

This project is intentionally designed as a **portfolio-grade DevOps project**

---

## Learning Objectives

- Understand DevOps in practice
- Containerize applications with Docker
- Implement CI using GitHub Actions
- Integrate GitHub with Microsoft Azure
- Handle secrets and credentials securely
- Verify artifacts in a cloud environment

---

## Tech Stack

- **OS:** macOS
- **Language:** Python 3.11
- **Framework:** FastAPI
- **Containerization:** Docker
- **Version Control:** Git & GitHub
- **CI/CD:** GitHub Actions
- **Cloud Platform:** Microsoft Azure (Azure for Students)
- **Registry:** Azure Container Registry (ACR)

---

## Azure Setup

Azure was configured using **Azure for Students**.

- **Tenant:** Kristiania
- **Subscription:** Azure for Students
- **Authentication:** Azure CLI

```bash
az login
az account show
```

Important note:
Some regions (e.g. West Europe) were restricted for ACR in the student subscription.
Norway East was selected for compatibility and stability.

---

## Project Structure

```text
azure-devops-project-1/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── requirements.txt
├── tests/
│   └── test_app.py
├── .github/
│   └── workflows/
│       └── docker-build.yml
├── Dockerfile
├── pytest.ini
├── .gitignore
└── README.md
```

---

## Application (FastAPI)

The application exposes two endpoints:

- `/` – service status and message
- `/health` – health check endpoint

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "message": "Azure DevOps Project 1 is running"}

@app.get("/health")
def health():
    return {"health": "healthy"}
```

Run locally:

```bash
python3 -m uvicorn app.main:app --reload
```

---

## Testing

Automated tests are implemented using pytest.

- Tests run locally
- Tests run in CI
- Docker build is blocked if tests fail

`pytest.ini`:

```ini
[pytest]
pythonpath = .
testpaths = tests
```

This enforces quality gates before any artifact is built or published.

---

## Containerization with Docker

The application is packaged as a lightweight Docker container.

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Local build and run:

```bash
docker build -t devops-app .
docker run -p 8000:8000 devops-app
```

---

## Azure Container Registry (ACR)

Azure Container Registry is used as a private image repository between CI and runtime.

- **Registry:** ayanledevopsacr1
- **Region:** Norway East
- **Tier:** Basic

Repositories appear only after the first successful image push via CI.

---

## GitHub Secrets

Secrets are used to authenticate GitHub Actions against Azure securely.

| Secret Name | Description |
| --- | --- |
| `ACR_LOGIN_SERVER` | Registry login server |
| `ACR_USERNAME` | Registry username |
| `ACR_PASSWORD` | Registry access key |

No credentials are stored in code or committed to the repository.

---

## Continuous Integration (GitHub Actions)

The CI pipeline is triggered on every push to `main`.

Pipeline flow:

- Run automated tests (pytest)
- Build Docker image
- Tag image (`latest` + commit SHA)
- Push image to Azure Container Registry

This ensures traceability, reproducibility, and code quality.

---

## Deployment to Azure Container Apps

The application is deployed using Azure Container Apps.

- Image pulled directly from ACR
- Managed Identity used for ACR pull
- HTTP ingress enabled (port 8000)
- Public endpoint available

---

## Continuous Deployment (CD) – Tenant Limitation

Full CD (GitHub → Azure deployment) using federated identity (OIDC) was evaluated.

However:

- Azure for Students uses a restricted Entra ID tenant
- Federated identity requires tenant-level permissions
- These permissions are not available in student tenants

Design decision:
CI is fully automated. Deployment is configured via Azure Portal.
This reflects real-world enterprise governance constraints.

---

## Outcome

- Automated CI pipeline in place
- Tests enforced before build
- Docker images built and published automatically
- Artifacts stored in Azure
- Application running successfully in the cloud

---

