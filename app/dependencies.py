from fastapi import Depends

from sqlalchemy.orm import Session

from app.domain.services.item_service import ItemService
from app.domain.services.user_service import UserService

from app.infrastructure.persistence.db.session import SessionLocal
from app.infrastructure.persistence.repository.user_repository import UserRepository
from app.infrastructure.persistence.repository.item_repository import ItemRepository


async def get_db() -> Session:
    _session = SessionLocal()
    try:
        yield _session
    finally:
        _session.close()


def get_item_service(db: Session = Depends(get_db)) -> ItemService:
    repo = ItemRepository(session=db)
    return ItemService(repository=repo)


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    repo = UserRepository(session=db)
    return UserService(repository=repo)
