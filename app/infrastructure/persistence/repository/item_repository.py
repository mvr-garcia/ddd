from psycopg2.extensions import connection

from app.domain.ports.item_repository_port import ItemRepositoryPort
from app.domain.entities.item import Item


class ItemRepository(ItemRepositoryPort):
    def __init__(self, database_connection: connection):
        self.database_connection = database_connection

    def add_item(self, item: Item) -> None:
        self.database_connection.execute(
            'INSERT INTO items (name, description) VALUES ($1, $2)',
            (item.name, item.description)
        )

    def get_item(self, item_id: int) -> Item:
        result = self.database_connection.fetch_one(
            'SELECT id, name, description FROM items WHERE id = $1',
            (item_id,)
        )
        if result:
            return Item(*result)
        else:
            raise ItemNotFoundError()

    def get_all_items(self) -> List[Item]:
        results = self.database_connection.fetch_all(
            'SELECT id, name, description FROM items'
        )
        return [Item(*result) for result in results]

    def update_item(self, item_id: int, item: Item) -> None:
        result = self.database_connection.execute(
            'UPDATE items SET name = $1, description = $2 WHERE id = $3',
            (item.name, item.description, item_id)
        )
