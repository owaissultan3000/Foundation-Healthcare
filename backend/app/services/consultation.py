from app.models.diagnosis import DiagnosisCode
from sqlalchemy.orm import Session
from app.models import Consultation
from app.schemas import ConsultationCreate
from app.utils.exceptions import handle_exceptions
from sqlalchemy import func



def create_consultation(db: Session, data: ConsultationCreate):
    try:
        # Create the consultation
        consultation = Consultation(
            patient_name=data.patient_name,
            notes=data.notes,
            diagnosis_code_id=data.diagnosis_code_id
        )
        db.add(consultation)
        db.commit()
        db.refresh(consultation)
        
        # Fetch the diagnosis code & description separately
        diagnosis = db.query(DiagnosisCode).filter(
            DiagnosisCode.id == consultation.diagnosis_code_id
        ).first()
        
        # Convert to dict and add diagnosis_code & description
        result = consultation.__dict__.copy()
        result['diagnosis_code'] = diagnosis.code if diagnosis else None
        result['description'] = diagnosis.description if diagnosis else None
        
        return result

    except Exception as exc:
        handle_exceptions(
            db,
            exc,
            message="Failed to create consultation"
        )


def list_consultations(
    db: Session,
    page: int = 1,
    page_size: int = 10
):
    try:
        offset = (page - 1) * page_size
        
        # Get total count
        total_count = db.query(func.count(Consultation.id)).scalar()
        
        # Get paginated data
        data =  (
            db.query(
                Consultation.id,
                Consultation.patient_name,
                Consultation.notes,
                Consultation.diagnosis_code_id,
                Consultation.created_at,
                DiagnosisCode.code.label("diagnosis_code"),
                DiagnosisCode.description.label("description")
            )
            .join(DiagnosisCode, Consultation.diagnosis_code_id == DiagnosisCode.id)
            .order_by(Consultation.created_at.desc())
            .offset(offset)
            .limit(page_size)
            .all()
        )
        
        # Calculate total pages
        total_pages = (total_count + page_size - 1)
        
        # Create response
        response_data = [
            {
                "id": item.id,
                "patient_name": item.patient_name,
                "notes": item.notes,
                "diagnosis_code_id": item.diagnosis_code_id,
                "diagnosis_code": item.diagnosis_code,
                "description": item.description,
                "created_at": item.created_at
            }
            for item in data
        ]
        
        return {
            "data": response_data,
            "pagination": {
                "total": total_count,
                "page": page,
                "page_size": page_size,
                "total_pages": total_pages
            }
        }

    except Exception as exc:
        handle_exceptions(
            db,
            exc,
            message="Failed to fetch consultations"
        )