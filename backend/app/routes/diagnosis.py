from fastapi import APIRouter, Depends, Query
from app.auth.dependencies import get_current_user
from sqlalchemy.orm import Session

from app.schemas.diagnosis import DiagnosisResponse
from app.services.diagnosis import (
    search_diagnosis,
    get_all_diagnoses,
)
from app.dependencies import get_db

router = APIRouter(
    prefix="/diagnosis",
    tags=["Diagnosis"],
)


@router.get("")
def search(
    search: str = Query(..., min_length=1),
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return search_diagnosis(db, search)


@router.get(
    "/all",
    response_model=list[DiagnosisResponse]
)
def fetch_all_diagnoses(
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return get_all_diagnoses(db)
