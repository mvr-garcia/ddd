from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgres://user:password@host:port/dbname')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
