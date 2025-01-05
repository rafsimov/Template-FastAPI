from sqlalchemy import Column, Integer, String
from database import Base  # Используем Base из database.py

class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
