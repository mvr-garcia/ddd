from abc import ABC, abstractmethod

from app.domain.entities.user import User
from app.domain.entities.item import Item


class IItemRepository(ABC):
    @abstractmethod
    async def add_item(self, item: Item) -> None:
        pass

    @abstractmethod
    async def get_item(self, item_id: int) -> Item:
        pass

    @abstractmethod
    async def get_all_items(self) -> list[Item]:
        pass

    @abstractmethod
    async def update_item(self, item: Item) -> None:
        pass

    @abstractmethod
    async def delete_item(self, item_id: int) -> None:
        pass


class IUserRepository(ABC):
    @abstractmethod
    async def add_user(self, user: User) -> None:
        pass

    @abstractmethod
    async def get_user(self, user_id: int) -> User:
        pass

    @abstractmethod
    async def update_user(self, user: User) -> None:
        pass

    @abstractmethod
    async def delete_user(self, user_id: int) -> None:
        pass
