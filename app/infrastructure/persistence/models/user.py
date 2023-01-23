from __future__ import annotations

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.infrastructure.persistence.db.base_class import Base
from app.domain.entities.user import User


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    items = relationship("ItemModel", back_populates="user")

    @classmethod
    def from_entity(cls, entity: User) -> UserModel:
        return cls(
            id=entity.id,
            name=entity.name,
            email=entity.email,
            password=entity.password
        )

    def to_entity(self) -> User:
        return User(
            id=self.id,
            name=self.name,
            email=self.email,
            password=self.password,
            items=[i.to_entity() for i in self.items]
        )
