from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routes import router
from app.database import init_db

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Hello from Math API"}

app = FastAPI(title="Math Microservice")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # vagy pl. ["http://localhost:5500"] ha csak onnan jön kérés
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.on_event("startup")
def startup():
    print("Initializing database...")
    init_db()
