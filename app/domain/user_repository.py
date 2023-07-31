from abc import ABC, abstractmethod

from .user import User

class UserRepository(ABC):
    @abstractmethod
    def create_user(self, user: User) -> User:
        pass