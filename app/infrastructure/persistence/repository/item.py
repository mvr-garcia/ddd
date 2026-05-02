from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.interfaces.repositories import IItemRepository
from app.domain.entities.item import Item
from app.infrastructure.persistence.models.item import ItemModel


class ItemRepository(IItemRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_item(self, item: Item) -> None:
        model = ItemModel(
            name=item.name,
            description=item.description,
            price=item.price,
            user_id=item.user.id,
        )
        self.session.add(model)
        await self.session.commit()

    async def get_item(self, item_id: int) -> Item:
        model = await self.session.query(ItemModel).get(item_id)
        return model.to_entity()

    async def update_item(self, item: Item) -> None:
        model = ItemModel(
            id=item.id,
            name=item.name,
            description=item.description,
            price=item.price,
            user_id=item.user.id,
        )
        self.session.add(model)
        await self.session.commit()

    async def delete_item(self, item_id: int) -> None:
        await self.session.query(ItemModel).filter(ItemModel.id == item_id).delete()
        await self.session.commit()
