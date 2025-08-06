# Структура проекта T3CodesCommanders

```
t3CodesCommanders/
├── 📁 t3codescommanders/          # Основной проект Django
│   ├── 📄 __init__.py
│   ├── 📄 settings.py             # Настройки проекта
│   ├── 📄 urls.py                 # Главные URL маршруты
│   ├── 📄 wsgi.py                 # WSGI конфигурация
│   ├── 📄 asgi.py                 # ASGI конфигурация
│   └── 📁 management/             # Пользовательские команды
│       ├── 📄 __init__.py
│       └── 📁 commands/
│           ├── 📄 __init__.py
│           └── 📄 wait_for_db.py  # Команда ожидания БД
│
├── 📁 users/                      # Приложение пользователей
│   ├── 📄 __init__.py
│   ├── 📄 apps.py                 # Конфигурация приложения
│   ├── 📄 models.py               # Модель User
│   ├── 📄 serializers.py          # Сериализаторы API
│   ├── 📄 views.py                # Представления API
│   ├── 📄 urls.py                 # URL маршруты
│   ├── 📄 admin.py                # Админка Django
│   └── 📁 migrations/             # Миграции базы данных
│       ├── 📄 __init__.py
│       └── 📄 0001_initial.py
│
├── 📁 orders/                     # Приложение заказов
│   ├── 📄 __init__.py
│   ├── 📄 apps.py                 # Конфигурация приложения
│   ├── 📄 models.py               # Модель Order
│   ├── 📄 serializers.py          # Сериализаторы API
│   ├── 📄 views.py                # Представления API
│   ├── 📄 urls.py                 # URL маршруты
│   ├── 📄 admin.py                # Админка Django
│   └── 📁 migrations/             # Миграции базы данных
│       ├── 📄 __init__.py
│       └── 📄 0001_initial.py
│
├── 📄 manage.py                   # Django management script
├── 📄 requirements.txt            # Зависимости Python
├── 📄 Dockerfile                  # Конфигурация Docker
├── 📄 docker-compose.yml          # Docker Compose
├── 📄 .gitignore                  # Git ignore файл
├── 📄 README.md                   # Основная документация
├── 📄 DEPLOYMENT.md               # Инструкции по развертыванию
├── 📄 test_api.py                 # Тесты API
├── 📄 PROJECT_STRUCTURE.md        # Этот файл
└── 📄 db.sqlite3                  # SQLite база данных (для разработки)
```

## Описание файлов

### Основные файлы проекта
- **`manage.py`** - Django management script для выполнения команд
- **`requirements.txt`** - Список Python зависимостей
- **`Dockerfile`** - Конфигурация Docker контейнера
- **`docker-compose.yml`** - Docker Compose для запуска с PostgreSQL
- **`.gitignore`** - Файлы, исключенные из Git

### Документация
- **`README.md`** - Основная документация проекта
- **`DEPLOYMENT.md`** - Подробные инструкции по развертыванию
- **`test_api.py`** - Автоматические тесты API
- **`PROJECT_STRUCTURE.md`** - Описание структуры проекта

### Настройки Django
- **`t3codescommanders/settings.py`** - Основные настройки Django
- **`t3codescommanders/urls.py`** - Главные URL маршруты
- **`t3codescommanders/wsgi.py`** - WSGI конфигурация для продакшна
- **`t3codescommanders/asgi.py`** - ASGI конфигурация для асинхронности

### Приложение Users
- **`users/models.py`** - Модель User с полями: name, email, age
- **`users/serializers.py`** - Сериализаторы для API пользователей
- **`users/views.py`** - API представления для CRUD операций
- **`users/urls.py`** - URL маршруты для API пользователей
- **`users/admin.py`** - Админка Django для управления пользователями

### Приложение Orders
- **`orders/models.py`** - Модель Order с полями: title, description, user
- **`orders/serializers.py`** - Сериализаторы для API заказов
- **`orders/views.py`** - API представления с проверкой существования пользователя
- **`orders/urls.py`** - URL маршруты для API заказов
- **`orders/admin.py`** - Админка Django для управления заказами

### Миграции
- **`users/migrations/`** - Миграции для модели User
- **`orders/migrations/`** - Миграции для модели Order

### Docker файлы
- **`Dockerfile`** - Многоэтапная сборка с Python 3.10
- **`docker-compose.yml`** - Оркестрация с PostgreSQL

## API Endpoints

### Users API
- `GET /api/users/` - Получить список пользователей
- `POST /api/users/` - Создать пользователя
- `GET /api/users/{id}/` - Получить пользователя
- `PUT /api/users/{id}/` - Обновить пользователя
- `DELETE /api/users/{id}/` - Удалить пользователя

### Orders API
- `GET /api/orders/` - Получить список заказов
- `POST /api/orders/` - Создать заказ
- `GET /api/orders/{id}/` - Получить заказ
- `PUT /api/orders/{id}/` - Обновить заказ
- `DELETE /api/orders/{id}/` - Удалить заказ
- `GET /api/users/{id}/orders/` - Получить заказы пользователя

## Технологии

- **Python 3.10+** - Основной язык программирования
- **Django 4.2.7** - Веб-фреймворк
- **Django REST Framework** - API фреймворк
- **PostgreSQL** - Основная база данных
- **SQLite** - База данных для разработки
- **Docker** - Контейнеризация
- **Docker Compose** - Оркестрация контейнеров

## Особенности реализации

### Безопасность
- ✅ Валидация данных на уровне моделей и сериализаторов
- ✅ Проверка существования пользователя при создании заказов
- ✅ Обработка ошибок с детальными сообщениями
- ✅ CORS настройки для фронтенда

### Производительность
- ✅ Оптимизированные запросы к базе данных
- ✅ Пагинация результатов
- ✅ Селективные запросы в админке

### Масштабируемость
- ✅ Модульная архитектура
- ✅ Разделение на приложения
- ✅ Готовность к контейнеризации
- ✅ Поддержка переменных окружения

### Разработка
- ✅ Автоматические тесты API
- ✅ Детальная документация
- ✅ Готовые инструкции по развертыванию
- ✅ Поддержка Docker для быстрого старта 