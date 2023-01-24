from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_db_session(engine):
    engine = create_engine('postgres://user:password@host:port/dbname')
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    _session = session()
    try:
        yield _session
    finally:
        _session.close()
