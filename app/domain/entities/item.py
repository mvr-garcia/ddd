from pydantic import BaseModel

from app.domain.entities.user import User


class Item(BaseModel):
    id: int
    name: str
    description: str
    price: int
    user: User
