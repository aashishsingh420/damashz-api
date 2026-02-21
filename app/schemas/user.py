from pydantic import BaseModel


class UserCreate(BaseModel):
    keycloak_id: str
    email: str


class UserResponse(BaseModel):
    id: int
    keycloak_id: str
    email: str

    class Config:
        from_attributes = True