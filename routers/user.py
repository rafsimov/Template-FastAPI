# routers/user.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from services import user as UserService
from dto import user as UserDTO

router = APIRouter()

@router.post('/', tags=['user'])
async def create(data: UserDTO.User, db: AsyncSession = Depends(get_db)):
    try:
        return await UserService.create_user(data, db)
    except HTTPException as e:
        raise e

@router.get('/{id}', tags=['user'])
async def get(id: int, db: AsyncSession = Depends(get_db)):
    try:
        return await UserService.get_user(id, db)
    except HTTPException as e:
        raise e

@router.put('/{id}', tags=['user'])
async def update(id: int, data: UserDTO.User, db: AsyncSession = Depends(get_db)):
    try:
        return await UserService.update(data, id, db)
    except HTTPException as e:
        raise e

@router.delete('/{id}', tags=['user'])
async def delete(id: int, db: AsyncSession = Depends(get_db)):
    try:
        return await UserService.remove(id, db)
    except HTTPException as e:
        raise e
