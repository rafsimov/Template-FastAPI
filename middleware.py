# middleware.py
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import HTTPException
import time
from logger import setup_logging

# Инициализируем логгер
logger = setup_logging()

# для тротлинга
request_times = {}
request_limit = 5  # Максимум 5 запросов
time_window = 60    # Время окна для тротлинга (в секундах)

class RequestLoggerAndThrottlingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        ip = request.client.host  # Получаем IP-адрес клиента
        current_time = time.time()

        # Логирование входящего запроса
        logger.info(f"Incoming request from IP {ip}: {request.method} {request.url} | Headers: {dict(request.headers)}")

        # Реализация тротлинга
        if ip in request_times:
            # Очистить старые записи (которые старше `time_window` секунд)
            request_times[ip] = [
                t for t in request_times[ip] if current_time - t <= time_window
            ]

        # Если количество запросов больше лимита, блокируем запрос
        if len(request_times.get(ip, [])) >= request_limit:
            logger.warning(f"IP {ip} exceeded request limit. Blocking further requests.")
            raise HTTPException(status_code=429, detail="Too many requests. Please try again later.")

        # Добавляем текущий запрос в историю времени для этого IP
        if ip not in request_times:
            request_times[ip] = []
        request_times[ip].append(current_time)

        # Обрабатываем запрос и получаем ответ
        response = await call_next(request)

        # Логируем информацию о ответе
        process_time = time.time() - current_time
        logger.info(f"Response for {ip}: {response.status_code} | Process time: {process_time:.4f}s")

        return response
