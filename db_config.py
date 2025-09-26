from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# from sqlalchemy_utils import database_exists, create_database


DATABASE_URL = "postgresql://user:1234@127.0.0.1:5523/fastapi"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def db_connection():
     db = SessionLocal()
     try:
          yield db
          
     finally:
          db.close()