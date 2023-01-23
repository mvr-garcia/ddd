from __future__ import annotations

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.infrastructure.persistence.db.base_class import Base  # noqa
from app.domain.entities.item import Item


class ItemModel(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("UserModel", back_populates="items")

    @classmethod
    def from_entity(cls, entity: Item) -> ItemModel:
        return cls(
            id=entity.id,
            name=entity.name,
            description=entity.description,
            price=entity.price
        )
