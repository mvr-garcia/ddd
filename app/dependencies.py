from fastapi import Depends

from app.domain.interfaces.uow import IUnitOfWork

from app.factories import get_settings
from app.infrastructure.persistence.db.session import get_engine, get_session_maker
from app.infrastructure.persistence.uow import UnitOfWork


async def get_uow(*, settings = Depends(get_settings)) -> IUnitOfWork:
    engine = await get_engine(settings)
    session_maker = await get_session_maker(engine=engine)
    return UnitOfWork(session_maker=session_maker)
