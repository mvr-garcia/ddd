from typing import Callable

from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.interfaces.uow import IUnitOfWork
from app.infrastructure.persistence.repository.item import ItemRepository
from app.infrastructure.persistence.repository.user import UserRepository



class UnitOfWork(IUnitOfWork):
    """
    Unit of Work implementation for managing database transactions and repositories.

    This class provides a context manager interface for managing database sessions
    and coordinating multiple repositories within a single transaction.
    """

    def __init__(
        self,
        *,
        session_factory: Callable[[], AsyncSession],
    ):
        """
        Initialize the Unit of Work.

        Args:
            session_factory: Callable that creates AsyncSession instances
        """
        self._session_factory = session_factory
        self.session: AsyncSession | None = None

    async def __aenter__(self):
        """
        Enter the async context manager.

        Creates a new session if one doesn't exist and initializes repositories.

        Returns:
            UnitOfWork: The Unit of Work instance itself
        """
        self.session = self._session_factory()
        self.item = ItemRepository(self.session)
        self.user = UserRepository(self.session)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        """
        Exit the async context manager.

        Handles cleanup: close session, rollback transaction, and close connection.

        Args:
            exc_type: Exception type if an exception occurred
            exc: Exception instance if an exception occurred
            tb: Traceback if an exception occurred
        """
        try:
            if exc:
                await self.session.rollback()
        finally:
            await self.session.close()

    async def commit(self):
        """
        Commit all changes in the current transaction.
        """
        await self.session.commit()

    async def rollback(self):
        """
        Rollback all changes in the current transaction.
        """
        await self.session.rollback()
