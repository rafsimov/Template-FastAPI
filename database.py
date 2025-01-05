from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select
import asyncio

# Создаем базовый класс для моделей
Base = declarative_base()

# URL для подключения к базе данных
SQLALCHEMY_URL = 'sqlite+aiosqlite:///./database.db'

# Создаем асинхронный движок
engine = create_async_engine(SQLALCHEMY_URL, connect_args={'check_same_thread': False})

# Асинхронная сессия
SessionLocal = sessionmaker(engine, class_=AsyncSession, autocommit=False, autoflush=False)

# Функция для получения сессии
async def get_db():
    async with SessionLocal() as db:  # Используем асинхронный контекстный менеджер
        yield db

# Создание таблиц асинхронно
async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
