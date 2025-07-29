from fastapi import FastAPI
from app.routes import router
from app.database import init_db

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Hello from Math API"}

app = FastAPI(title="Math Microservice")

app.include_router(router)


@app.on_event("startup")
def startup():
    print("Initializing database...")
    init_db()
