from app.domain.entities.item import Item


class ItemRepositoryPort:
    def add_item(self, item: Item) -> None:
        raise NotImplementedError()

    def get_item(self, item_id: int) -> Item:
        raise NotImplementedError()

    def get_all_items(self) -> list[Item]:
        raise NotImplementedError()

    def update_item(self, item_id: int, item: Item) -> None:
        raise NotImplementedError()

    def delete_item(self, item_id: int) -> None:
        raise NotImplementedError()
