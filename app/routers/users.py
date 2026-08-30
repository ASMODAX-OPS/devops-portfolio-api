from fastapi import APIRouter, HTTPException
from app.schemas import UserCreate, UserResponse
from app.storage import user_storage

router = APIRouter(prefix="/api/users", tags=["users"])

@router.get("", response_model=list[UserResponse])
def list_users():
    return user_storage.get_all()

@router.post("", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate):
    return user_storage.create(user)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    user = user_storage.get_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
    return user