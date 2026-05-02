from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.entities.user import User
from app.domain.interfaces.repositories import IUserRepository
from app.infrastructure.persistence.models.user import UserModel


class UserRepository(IUserRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_user(self, user: User) -> None:
        model = UserModel(
            name=user.name,
            email=user.email,
            password=user.password,
        )
        self.session.add(model)
        await self.session.commit()

    async def get_user(self, user_id: int) -> User:
        user = await self.session.query(UserModel).get(user_id)
        return user.to_entity()

    async def update_user(self, user: User) -> None:
        model = UserModel(
            id=user.id,
            name=user.name,
            email=user.email,
            password=user.password,
        )
        self.session.add(model)
        await self.session.commit()

    async def delete_user(self, user_id: int) -> None:
        await self.session.query(UserModel).filter(UserModel.id == user_id).delete()
        await self.session.commit()
