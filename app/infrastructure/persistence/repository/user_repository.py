from sqlalchemy.orm import Session

from app.domain.entities.user import User
from app.domain.ports.user_repository_port import UserRepositoryPort
from app.infrastructure.persistence.models.user import UserModel


class UserRepository(UserRepositoryPort):

    def __init__(self, session: Session):
        self.session = session

    async def add_user(self, user: User) -> None:
        model = UserModel(
            name=user.name,
            email=user.email,
            password=user.password,
        )
        self.session.add(model)
        self.session.commit()

    async def get_user(self, user_id: int) -> User:
        user = self.session.query(UserModel).get(user_id)
        return user.to_entity()

    async def update_user(self, user: User) -> None:
        model = UserModel(
            id=user.id,
            name=user.name,
            email=user.email,
            password=user.password,
        )
        self.session.add(model)
        self.session.commit()

    async def delete_user(self, user_id: int) -> None:
        self.session.query(UserModel).filter(UserModel.id == user_id).delete()
