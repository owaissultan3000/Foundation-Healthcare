from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger(__name__)

class NotFoundError(Exception):
    def __init__(self, message: str = "Resource not found"):
        self.message = message
        super().__init__(self.message)


def handle_exceptions(
    db: Session,
    exc: Exception,
    message: str = "Database operation failed"
):
    db.rollback()
    logger.exception(exc)

    if isinstance(exc, NotFoundError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exc.message
        )

    if isinstance(exc, IntegrityError):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Integrity constraint violated"
        )

    if isinstance(exc, SQLAlchemyError):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=message
        )

    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Unexpected server error"
    )
