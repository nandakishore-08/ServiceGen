from fastapi import FastAPI
from app.routes.health_routes import router as health_router

app = FastAPI(title="ServiceGen")

app.include_router(health_router)

@app.get("/")
def home():
    return {"message": "Welcome to ServiceGen"}