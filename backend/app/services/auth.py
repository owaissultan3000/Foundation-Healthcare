from datetime import timedelta
from app.auth.auth import hash_password, verify_password
from app.models.user import User
from app.utils.exceptions import NotFoundError, handle_exceptions
from app.schemas.auth import RegisterRequest
from sqlalchemy.orm import Session
from app.auth.jwt import create_access_token, create_refresh_token
from sqlalchemy.exc import IntegrityError as SAIntegrityError



def authenticate_doctor(db: Session, email: str, password: str):
    doctor = db.query(User).filter(User.email == email).first()

    if not doctor or not verify_password(password, doctor.hashed_password):
        raise NotFoundError("Invalid email or password")

    access_token = create_access_token(
        data={"sub": str(doctor.id)},
        expires_delta=timedelta(minutes=15)
    )

    refresh_token = create_refresh_token(
        data={"sub": str(doctor.id)},
        expires_delta=timedelta(days=7)
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

def register_user(db: Session, payload: RegisterRequest):
    try:
        user = User(
            first_name=payload.first_name,
            last_name= payload.last_name or '',
            email=payload.email,
            hashed_password=hash_password(payload.password),
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    except SAIntegrityError as exc:
        db.rollback()
        handle_exceptions(
            db,
            exc,
            message="Email already exists"
        )
