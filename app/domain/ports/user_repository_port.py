from app.domain.entities.user import User


class UserRepositoryPort:
    def add_user(self, user: User) -> None:
        raise NotImplementedError()

    def get_user(self, user_id: int) -> User:
        raise NotImplementedError()

    def update_user(self, user: User) -> None:
        raise NotImplementedError()

    def delete_user(self, user_id: int) -> None:
        raise NotImplementedError()
