from app.domain.entities.item import Item


class ItemRepositoryPort:
    async def add_item(self, item: Item) -> None:
        raise NotImplementedError()

    async def get_item(self, item_id: int) -> Item:
        raise NotImplementedError()

    async def get_all_items(self) -> list[Item]:
        raise NotImplementedError()

    async def update_item(self, item: Item) -> None:
        raise NotImplementedError()

    async def delete_item(self, item_id: int) -> None:
        raise NotImplementedError()
