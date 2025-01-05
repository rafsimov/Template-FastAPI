# main.py
import uvicorn
from fastapi import FastAPI
from database import create_db
from routers import user as UserRouter
from middleware import RequestLoggerAndThrottlingMiddleware

# Асинхронная функция для жизненного цикла приложения
async def lifespan(app: FastAPI):
    # Логика при старте приложения
    await create_db()  # Создание базы данных
    print("DB was created!")
    yield  # Приложение работает здесь
    # Логика при остановке приложения
    print("Shutting down app...")

# Создание FastAPI приложения с lifespan
app = FastAPI(lifespan=lifespan)

# Подключаем middleware для логирования и тротлинга
app.add_middleware(RequestLoggerAndThrottlingMiddleware)

# Включаем роутер для пользователей
app.include_router(UserRouter.router, prefix='/user')

# Запуск приложения
if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)
