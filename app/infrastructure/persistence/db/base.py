# Import all the models, so that Base has them before being
# imported by Alembic
from app.infrastructure.persistence.db.base_class import Base  # noqa
from app.infrastructure.persistence.models.item import ItemModel  # noqa
from app.infrastructure.persistence.models.user import UserModel  # noqa
