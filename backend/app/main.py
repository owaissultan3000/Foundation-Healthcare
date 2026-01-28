from fastapi import FastAPI, Depends, Query
from app.database import SessionLocal, engine
from app.database import Base
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, consultation, diagnosis
from app.seed import seed_diagnosis_codes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ClinicCare")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    db = SessionLocal()
    seed_diagnosis_codes(db)
    db.close()


@app.get("/")
def health():
    return {"status": "ok"}


# Routes
app.include_router(auth.router)
app.include_router(consultation.router)
app.include_router(diagnosis.router)