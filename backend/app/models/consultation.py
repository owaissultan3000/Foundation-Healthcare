from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Consultation(Base):
    __tablename__ = "consultations"

    id = Column(Integer, primary_key=True)
    patient_name = Column(String, nullable=False)
    notes = Column(Text, nullable=False)

    diagnosis_code_id = Column(
        Integer,
        ForeignKey("diagnosis_codes.id"),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    diagnosis_code = relationship("DiagnosisCode")
