from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import MYSQL_URL

engine = create_engine(MYSQL_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()