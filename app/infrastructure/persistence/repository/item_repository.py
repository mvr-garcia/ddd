from sqlalchemy.orm import Session

from app.domain.ports.item_repository_port import ItemRepositoryPort
from app.domain.entities.item import Item
from app.infrastructure.persistence.models.item import ItemModel


class ItemRepository(ItemRepositoryPort):

    def __init__(self, session: Session):
        self.session = session

    async def add_item(self, item: Item) -> None:
        model = ItemModel(
            name=item.name,
            description=item.description,
            price=item.price,
            user_id=item.user.id,
        )
        self.session.add(model)
        self.session.commit()

    async def get_item(self, item_id: int) -> Item:
        model = self.session.query(ItemModel).get(item_id)
        return model.to_entity()

    async def update_item(self, item: Item) -> None:
        model = ItemModel(
            id=id,
            name=item.name,
            description=item.description,
            price=item.price,
            user_id=item.user.id,
        )
        self.session.add(model)
        self.session.commit()

    async def delete_item(self, item_id: int) -> None:
        self.session.query(ItemModel).filter(ItemModel.id == item_id).delete()
        self.session.commit()
