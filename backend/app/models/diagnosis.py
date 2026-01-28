from sqlalchemy import Column, Integer, String
from app.database import Base

class DiagnosisCode(Base):
    __tablename__ = "diagnosis_codes"

    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=False)
