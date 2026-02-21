from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user, get_all_users

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user.keycloak_id, user.email)


@router.get("/", response_model=list[UserResponse])
def list_users_endpoint(db: Session = Depends(get_db)):
    return get_all_users(db)