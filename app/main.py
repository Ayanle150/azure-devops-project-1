from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "message": "Azure DevOps Project 1 is running"}

@app.get("/health")
def health():
    return {"health": "healthy"}
