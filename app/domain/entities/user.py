from pydantic import BaseModel

from app.domain.entities.item import Item


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    items: list[Item]
