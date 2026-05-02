from app.domain.entities.user import User
from app.domain.ports.user_repository_port import UserRepositoryPort


class UserService:
    def __init__(self, repository: UserRepositoryPort):
        self.repository = repository

    def get_user(self, user_id: int) -> User:
        return self.repository.get_user(user_id)

    def get_users(self) -> list[User]:
        return self.repository.get_users()

    def create_user(self, name: str, email: str) -> User:
        if not name or not email:
            raise ValueError("Name and email are required.")

        if self.repository.get_user_by_email(email):
            raise ValueError("Email already in use.")

        user = User(name=name, email=email)
        return self.repository.create_user(user)

    def update_user(self, user_id: int, name: str, email: str) -> User:
        if not name or not email:
            raise ValueError("Name and email are required.")

        user = self.repository.get_user(user_id)
        if self.repository.get_user_by_email(email) and user.email != email:
            raise ValueError("Email already in use.")

        user.name = name
        user.email = email
        return self.repository.update_user(user)
