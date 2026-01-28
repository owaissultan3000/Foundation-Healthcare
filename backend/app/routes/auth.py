from datetime import timedelta
from http.client import HTTPException
from app.models.user import User
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from app.auth.jwt import SECRET_KEY, ALGORITHM, create_access_token
from app.schemas.auth import LoginRequest, RefreshTokenRequest, RegisterRequest, TokenResponse
from app.services.auth import authenticate_doctor, register_user
from app.dependencies import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    return authenticate_doctor(db, data.email, data.password)


@router.post("/register", status_code=201)
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    user = register_user(db, data)
    return {
        "id": user.id,
        "email": user.email,
        "message": "User registered successfully"
    }

@router.post("/refresh")
def refresh_access_token(payload: RefreshTokenRequest, db: Session = Depends(get_db)):
    try:
        refresh_token = payload.refresh_token
        payload = jwt.decode(
            refresh_token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        if payload.get("type") != "refresh":
            raise HTTPException(status_code=401, detail="Invalid token type")

        user_id = payload.get("sub")
        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        access_token = create_access_token(
            data={"sub": str(user.id)},
            expires_delta=timedelta(minutes=15)
        )

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired refresh token")
