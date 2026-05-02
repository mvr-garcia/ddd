from app.domain.entities.item import Item
from app.domain.ports.item_repository_port import ItemRepositoryPort


class ItemService:

    async def __init__(self, repository: ItemRepositoryPort):
        self.repository = repository

    async def create(self, item: Item) -> Item:
        if item.price <= 0:
            raise ValueError("Price should be greater than zero")
        return await self.repository.add_item(item)

    async def get(self, item_id: int) -> Item:
        item = await self.repository.get_item(item_id)
        if not item:
            raise ValueError(f"Item not found with id: {item_id}")
        return item

    async def update(self, item: Item) -> Item:
        if item.price <= 0:
            raise ValueError("Price should be greater than zero")
        return await self.repository.update_item(item)

    async def delete(self, item_id: int):
        item = await self.repository.get_item(item_id)
        if not item:
            raise ValueError(f"Item not found with id: {item_id}")
        await self.repository.delete_item(item_id)
