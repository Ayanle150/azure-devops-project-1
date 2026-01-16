from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Version 2 deployed 🚀",
        "day": "Day 4 - Continuous Deployment"
    }

@app.get("/health")
def health():
    return {"health": "healthy"}
