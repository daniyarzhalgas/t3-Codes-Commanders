# T3CodesCommanders - Django REST API

Серверное приложение на Django с REST API для управления пользователями и заказами.

## Описание

Приложение реализует монолитную архитектуру с использованием:
- **Python 3.10+**
- **Django 4.2.7**
- **PostgreSQL**
- **Django REST Framework**
- **Docker**

## Функциональность

### Пользователи (Users)
- ✅ Хранение информации о пользователях (имя, email, возраст)
- ✅ API для добавления, получения и обновления пользователей
- ✅ Валидация данных (email, возраст)
- ✅ Обработка ошибок

### Заказы (Orders)
- ✅ Хранение информации о заказах (название, описание, ID пользователя)
- ✅ API для создания, получения и обновления заказов
- ✅ Проверка существования пользователя при создании заказа
- ✅ Получение заказов конкретного пользователя

## Структура проекта

```
t3CodesCommanders/
├── t3codescommanders/          # Основной проект Django
│   ├── settings.py             # Настройки проекта
│   ├── urls.py                 # Главные URL маршруты
│   └── management/             # Пользовательские команды
├── users/                      # Приложение пользователей
│   ├── models.py               # Модель User
│   ├── serializers.py          # Сериализаторы API
│   ├── views.py                # Представления API
│   └── urls.py                 # URL маршруты пользователей
├── orders/                     # Приложение заказов
│   ├── models.py               # Модель Order
│   ├── serializers.py          # Сериализаторы API
│   ├── views.py                # Представления API
│   └── urls.py                 # URL маршруты заказов
├── requirements.txt            # Зависимости Python
├── Dockerfile                  # Конфигурация Docker
├── docker-compose.yml          # Docker Compose
└── README.md                   # Документация
```

## API Endpoints

### Пользователи
- `GET /api/users/` - Получить список всех пользователей
- `POST /api/users/` - Создать нового пользователя
- `GET /api/users/{id}/` - Получить пользователя по ID
- `PUT /api/users/{id}/` - Обновить пользователя
- `DELETE /api/users/{id}/` - Удалить пользователя

### Заказы
- `GET /api/orders/` - Получить список всех заказов
- `POST /api/orders/` - Создать новый заказ
- `GET /api/orders/{id}/` - Получить заказ по ID
- `PUT /api/orders/{id}/` - Обновить заказ
- `DELETE /api/orders/{id}/` - Удалить заказ
- `GET /api/users/{id}/orders/` - Получить заказы пользователя

### Документация API
- API доступен по адресу: http://localhost:8000/api/
- Для тестирования используйте файл `test_api.py`

## Установка и запуск

### Способ 1: Docker Compose (Рекомендуется)

1. **Клонируйте репозиторий:**
   ```bash
   git clone <repository-url>
   cd t3CodesCommanders
   ```

2. **Запустите приложение с Docker Compose:**
   ```bash
   docker-compose up --build
   ```

3. **Приложение будет доступно по адресу:**
   - API: http://localhost:8000/api/
   - Документация: http://localhost:8000/api/docs/
   - Админка: http://localhost:8000/admin/

### Способ 2: Локальная установка

1. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Настройте PostgreSQL:**
   - Создайте базу данных `t3codescommanders`
   - Настройте переменные окружения или отредактируйте `settings.py`

3. **Выполните миграции:**
   ```bash
   python manage.py migrate
   ```

4. **Создайте суперпользователя (опционально):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Запустите сервер:**
   ```bash
   python manage.py runserver
   ```

## Переменные окружения

Создайте файл `.env` в корне проекта:

```env
# База данных
DB_NAME=t3codescommanders
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432

# Django
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# CORS
CORS_ALLOW_ALL_ORIGINS=True
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

## Примеры использования API

### Создание пользователя
```bash
curl -X POST http://localhost:8000/api/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Иван Иванов",
    "email": "ivan@example.com",
    "age": 25
  }'
```

### Создание заказа
```bash
curl -X POST http://localhost:8000/api/orders/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Заказ на разработку",
    "description": "Требуется разработать веб-приложение",
    "user": 1
  }'
```

### Получение заказов пользователя
```bash
curl -X GET http://localhost:8000/api/users/1/orders/
```

## Тестирование

Для тестирования API можно использовать:
- **Postman**
- **curl**
- **Swagger UI** (http://localhost:8000/api/docs/)

## Дополнительные возможности

- ✅ Пагинация результатов
- ✅ Детальная обработка ошибок
- ✅ Валидация данных
- ✅ CORS настройки
- ✅ Админка Django
- ✅ Docker контейнеризация
- ✅ Автоматическое ожидание базы данных

