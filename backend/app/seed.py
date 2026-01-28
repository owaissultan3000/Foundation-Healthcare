from sqlalchemy.orm import Session
from sqlalchemy import text
from pathlib import Path
from app.models import DiagnosisCode

def seed_diagnosis_codes(db: Session):
    if db.query(DiagnosisCode).first():
        return

    seed_file = Path("app/seed.sql")
    sql = seed_file.read_text()

    db.execute(text(sql))
    db.commit()
