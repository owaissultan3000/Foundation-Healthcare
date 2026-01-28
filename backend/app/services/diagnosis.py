from sqlalchemy.orm import Session
from app.models import DiagnosisCode
from app.utils.exceptions import NotFoundError, handle_exceptions


def search_diagnosis(db: Session, term: str):
    try:
        diagnosis =  (
            db.query(DiagnosisCode)
            .filter(
                DiagnosisCode.code.ilike(f"%{term}%")
            )
            .all()
        )

        if not diagnosis:
            raise NotFoundError(
                "No result found with given code"
            )
        
        return diagnosis

    except Exception as exc:
        handle_exceptions(
            db,
            exc,
            message="Failed to search diagnosis codes"
        )


def get_all_diagnoses(db: Session):
    try:
        return (
            db.query(DiagnosisCode)
            .order_by(DiagnosisCode.code)
            .all()
        )

    except Exception as exc:
        handle_exceptions(
            db,
            exc,
            message="Failed to fetch diagnosis codes"
        )
