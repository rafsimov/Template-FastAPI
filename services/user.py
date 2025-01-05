# services/user.py
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from models.user import User
from dto import user
from logger import setup_logging  # Импортируем настройку логгера

# Инициализируем логгер
logger = setup_logging()

async def create_user(data: user.User, db: Session):
    try:
        user_instance = User(name=data.name)
        db.add(user_instance)
        await db.commit()
        await db.refresh(user_instance)
        return user_instance
    except SQLAlchemyError as e:
        db.rollback()  # Откатываем изменения в случае ошибки
        logger.error(f"Error during user creation: {e}")  # Логируем ошибку
        raise HTTPException(status_code=500, detail="Error during user creation")

async def get_user(id: int, db: Session):
    try:
        result = await db.execute(select(User).filter(User.id == id))
        return result.scalar_one_or_none()
    except SQLAlchemyError as e:
        logger.error(f"Error during user retrieval: {e}")
        raise HTTPException(status_code=500, detail="Error during user retrieval")

async def update(data: user.User, id: int, db: Session):
    try:
        result = await db.execute(select(User).filter(User.id == id))
        user_instance = result.scalar_one_or_none()

        if user_instance:
            user_instance.name = data.name
            await db.commit()
            await db.refresh(user_instance)
            return user_instance
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error during user update: {e}")
        raise HTTPException(status_code=500, detail="Error during user update")

async def remove(id: int, db: Session):
    try:
        result = await db.execute(select(User).filter(User.id == id))
        user_instance = result.scalar_one_or_none()

        if user_instance:
            await db.delete(user_instance)
            await db.commit()
            return user_instance
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error during user removal: {e}")
        raise HTTPException(status_code=500, detail="Error during user removal")
