from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

from app.models.user import User


def create_user(db: Session, keycloak_id: str, email: str) -> User:
    user = User(keycloak_id=keycloak_id, email=email)

    db.add(user)

    try:
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email or keycloak_id already exists",
        )


def get_all_users(db: Session):
    return db.query(User).all()