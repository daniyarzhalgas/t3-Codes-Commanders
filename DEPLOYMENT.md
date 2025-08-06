# Инструкции по развертыванию T3CodesCommanders

## Быстрый старт с Docker Compose

### Предварительные требования
- Docker
- Docker Compose

### Шаги развертывания

1. **Клонируйте репозиторий:**
   ```bash
   git clone <repository-url>
   cd t3CodesCommanders
   ```

2. **Запустите приложение:**
   ```bash
   docker-compose up --build
   ```

3. **Приложение будет доступно:**
   - API: http://localhost:8000/api/
   - Админка: http://localhost:8000/admin/

## Локальное развертывание

### Предварительные требования
- Python 3.10+
- PostgreSQL 13+
- pip

### Шаги развертывания

1. **Создайте виртуальное окружение:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # или
   venv\Scripts\activate     # Windows
   ```

2. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Настройте PostgreSQL:**
   ```sql
   CREATE DATABASE t3codescommanders;
   CREATE USER t3user WITH PASSWORD 'your_password';
   GRANT ALL PRIVILEGES ON DATABASE t3codescommanders TO t3user;
   ```

4. **Создайте файл .env:**
   ```env
   DB_NAME=t3codescommanders
   DB_USER=t3user
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=5432
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ```

5. **Выполните миграции:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Создайте суперпользователя:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Запустите сервер:**
   ```bash
   python manage.py runserver
   ```

## Тестирование

### Автоматическое тестирование
```bash
python test_api.py
```

### Ручное тестирование с curl

**Создание пользователя:**
```bash
curl -X POST http://localhost:8000/api/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Иван Иванов",
    "email": "ivan@example.com",
    "age": 25
  }'
```

**Создание заказа:**
```bash
curl -X POST http://localhost:8000/api/orders/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Заказ на разработку",
    "description": "Требуется разработать веб-приложение",
    "user": 1
  }'
```

**Получение заказов пользователя:**
```bash
curl -X GET http://localhost:8000/api/users/1/orders/
```

## Мониторинг и логи

### Просмотр логов Docker
```bash
docker-compose logs -f web
docker-compose logs -f db
```

### Проверка состояния контейнеров
```bash
docker-compose ps
```

## Резервное копирование

### База данных
```bash
# Создание бэкапа
docker-compose exec db pg_dump -U postgres t3codescommanders > backup.sql

# Восстановление
docker-compose exec -T db psql -U postgres t3codescommanders < backup.sql
```

## Обновление приложения

1. **Остановите контейнеры:**
   ```bash
   docker-compose down
   ```

2. **Обновите код:**
   ```bash
   git pull origin main
   ```

3. **Пересоберите и запустите:**
   ```bash
   docker-compose up --build
   ```

## Устранение неполадок

### Проблема: Ошибка подключения к базе данных
**Решение:**
```bash
# Проверьте статус PostgreSQL
docker-compose ps

# Перезапустите базу данных
docker-compose restart db
```

### Проблема: Ошибки миграции
**Решение:**
```bash
# Удалите и пересоздайте базу данных
docker-compose down -v
docker-compose up --build
```

### Проблема: Порт 8000 занят
**Решение:**
```bash
# Измените порт в docker-compose.yml
ports:
  - "8001:8000"  # Используйте порт 8001
```

## Безопасность

### Продакшн настройки
1. Измените `DEBUG=False` в настройках
2. Установите сильный `SECRET_KEY`
3. Настройте `ALLOWED_HOSTS`
4. Используйте HTTPS
5. Настройте файрвол

### Переменные окружения для продакшна
```env
DEBUG=False
SECRET_KEY=your-very-secure-secret-key
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
DB_PASSWORD=very-secure-password
```

## Производительность

### Оптимизация для продакшна
1. Используйте Gunicorn вместо runserver
2. Настройте Nginx как прокси
3. Включите кэширование
4. Оптимизируйте запросы к базе данных

### Пример Gunicorn конфигурации
```bash
pip install gunicorn
gunicorn t3codescommanders.wsgi:application --bind 0.0.0.0:8000 --workers 4
``` 