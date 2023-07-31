from app.domain.user import User
from app.domain.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user: User):
        return self.user_repository.create_user(user)