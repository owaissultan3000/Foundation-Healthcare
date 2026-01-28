from app.auth.dependencies import get_current_user
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.schemas.consultation import (
    ConsultationCreate,
    ConsultationListResponse,
    ConsultationResponse,
)
from app.services.consultation import (
    create_consultation,
    list_consultations,
)
from app.dependencies import get_db

router = APIRouter(
    prefix="/consultation",
    tags=["Consultation"],
)


@router.post(
    "",
    response_model=ConsultationResponse
)
def create(
    consultation: ConsultationCreate,
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return create_consultation(db, consultation)


@router.get(
    "",
    response_model=ConsultationListResponse
)
def list_all(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return list_consultations(db, page, page_size)

