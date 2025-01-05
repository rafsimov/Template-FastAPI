# FastAPI шаблон
<p align="center">
  <a href="README.md">English</a>
  <a href="README.ru.md">Русский</a> |
</p>
Шаблон backend rest-api для вашего проекта, система тротлинга логов все есть

## Требования

Перед тем как запустить проект, убедитесь, что у вас установлены следующие зависимости:

- Python 3.8+
- pip

## Установка и настройка

### 1. Клонируйте репозиторий

Клонируйте репозиторий на ваш локальный компьютер:

```bash
git clone [https://github.com/rafsimov/=](https://github.com/rafsimov/Template-FastAPI)
cd template-fastapi
```
```bash
pip install -r requirements.txt
```
- И все заходите на http://localhost:8000/docs и отправляете запросы)

4. Доступ к документации API 📑
После того как сервер будет запущен, вы можете открыть документацию API по адресу http://localhost:8000/docs.


Документация автоматически сгенерируется FastAPI, и вы сможете отправлять запросы прямо из браузера.

Пример запроса:
Создание пользователя:
```bash
Копировать код
curl -X 'POST' \
  'http://localhost:8000/user/' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Dol Baeb"
}'
```
Получение пользователя:
```bash
curl -X 'GET' 'http://localhost:8000/user/1'
```
Обновление пользователя:
```bash
curl -X 'PUT' \
  'http://localhost:8000/user/1' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Dol Baeb"
}'
```
Удаление пользователя:
```bash
curl -X 'DELETE' 'http://localhost:8000/user/1'
```

## 📝 Логирование

Логи запросов и ответов будут записываться как в консоль, так и в файл `app.log`. В логе будут указаны:

- 🌍 **IP-адрес клиента**
- 🔄 **Метод запроса** (GET, POST, PUT, DELETE)
- 📡 **URL запроса**
- ✅❌ **Статус ответа**
- ⏱️ **Время обработки запроса**

Кроме того, будет отслеживаться количество запросов от одного IP (для защиты от спама). Если количество запросов превышает заданный лимит, сервер возвращает ошибку 429 (Too Many Requests).


## 🗂 Структура проекта

```plaintext
my-fastapi-project/
├── app/                       # Папка с основной логикой приложения
│   ├── main.py                # Основной файл для запуска приложения
│ ├───── logger.py             # Файл, отвечающий за настройку и работу с функцией ведения логов
│   ├── middleware.py          # Middleware для логирования и тротлинга
│   ├── database.py            # Логика работы с базой данных
│   ├── routers/               # Папка с роутерами для различных сущностей (например, users)
│   │   └── user.py     # Роутер для сущности пользователя
│   ├── models/                # Модели для базы данных
│   │   └── user.py      # Модель пользователя
│   ├── services/              # Логика для работы с данными и базой
│   │   └── user.py    # Сервис для пользователя
├── requirements.txt           # Все зависимости проекта
├── app.log                    # Лог-файл для хранения логов приложения
└── README.md                  # Документация проекта