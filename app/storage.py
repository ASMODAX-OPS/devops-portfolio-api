from typing import Optional
from app.schemas import UserCreate, UserResponse

class UserStorage:
    def __init__(self):
        self._users: dict[int, UserResponse] = {}
        self._next_id = 1

    def create(self, user: UserCreate) -> UserResponse:
        new_user = UserResponse(id=self._next_id, name=user.name, email=user.email)
        self._users[self._next_id] = new_user
        self._next_id += 1
        return new_user

    def get_all(self) -> list[UserResponse]:
        return list(self._users.values())

    def get_by_id(self, user_id: int) -> Optional[UserResponse]:
        return self._users.get(user_id)

user_storage = UserStorage()