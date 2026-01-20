import os
from fastapi import FastAPI

app = FastAPI()

APP_VERSION = os.getenv("APP_VERSION", "dev")
GIT_SHA = os.getenv("GIT_SHA", "local")

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Azure DevOps Project 1 is running",
        "version": APP_VERSION,
        "git_sha": GIT_SHA,
    }

@app.get("/health")
def health():
    return {"health": "healthy", "version": APP_VERSION}
