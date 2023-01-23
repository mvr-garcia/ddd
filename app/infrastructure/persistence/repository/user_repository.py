from app.domain.ports.user_repository_port import UserRepositoryPort
from app.domain.entities.user import User


class UserRepository(UserRepositoryPort):

    def __init__(self, connection_pool: AbstractConnectionPool):
        self.Session = scoped_session(sessionmaker(bind=connection_pool))

    def add_user(self, user: User):
        session = self.Session()
        session.add(user)
        session.commit()
        session.close()

    def get_user(self, user_id: int):
        session = self.Session()
        user = session.query(User).get(user_id)
        session.close()
        return user

    def update_user(self, user: User):
        session = self.Session()
        session.commit()
        session.close()

    def delete_user(self, user_id: int):
        session = self.Session()
        user = self.get_user(user_id)
        session.delete(user)
        session.commit()
        session.close()
