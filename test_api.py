#!/usr/bin/env python3
"""
Примеры тестирования API для T3CodesCommanders
"""

import requests
import json

BASE_URL = "http://localhost:8000/api"

def test_users_api():
    """Тестирование API пользователей"""
    print("=== Тестирование API пользователей ===")
    
    # Создание пользователя
    user_data = {
        "name": "Иван Иванов",
        "email": "ivan@example.com",
        "age": 25
    }
    
    print("1. Создание пользователя...")
    response = requests.post(f"{BASE_URL}/users/", json=user_data)
    print(f"Статус: {response.status_code}")
    print(f"Ответ: {response.json()}")
    
    if response.status_code == 201:
        user_id = response.json()['data']['id']
        
        # Получение пользователя
        print("\n2. Получение пользователя...")
        response = requests.get(f"{BASE_URL}/users/{user_id}/")
        print(f"Статус: {response.status_code}")
        print(f"Ответ: {response.json()}")
        
        # Обновление пользователя
        print("\n3. Обновление пользователя...")
        update_data = {"age": 26}
        response = requests.put(f"{BASE_URL}/users/{user_id}/", json=update_data)
        print(f"Статус: {response.status_code}")
        print(f"Ответ: {response.json()}")
        
        return user_id
    
    return None

def test_orders_api(user_id):
    """Тестирование API заказов"""
    print("\n=== Тестирование API заказов ===")
    
    # Создание заказа
    order_data = {
        "title": "Заказ на разработку",
        "description": "Требуется разработать веб-приложение с использованием Django и PostgreSQL",
        "user": user_id
    }
    
    print("1. Создание заказа...")
    response = requests.post(f"{BASE_URL}/orders/", json=order_data)
    print(f"Статус: {response.status_code}")
    print(f"Ответ: {response.json()}")
    
    if response.status_code == 201:
        order_id = response.json()['data']['id']
        
        # Получение заказа
        print("\n2. Получение заказа...")
        response = requests.get(f"{BASE_URL}/orders/{order_id}/")
        print(f"Статус: {response.status_code}")
        print(f"Ответ: {response.json()}")
        
        # Обновление заказа
        print("\n3. Обновление заказа...")
        update_data = {"title": "Обновленный заказ на разработку"}
        response = requests.put(f"{BASE_URL}/orders/{order_id}/", json=update_data)
        print(f"Статус: {response.status_code}")
        print(f"Ответ: {response.json()}")
        
        # Получение заказов пользователя
        print("\n4. Получение заказов пользователя...")
        response = requests.get(f"{BASE_URL}/users/{user_id}/orders/")
        print(f"Статус: {response.status_code}")
        print(f"Ответ: {response.json()}")
        
        return order_id
    
    return None

def test_error_handling():
    """Тестирование обработки ошибок"""
    print("\n=== Тестирование обработки ошибок ===")
    
    # Попытка создать пользователя с неверными данными
    print("1. Создание пользователя с неверным email...")
    invalid_user_data = {
        "name": "Тест",
        "email": "invalid-email",
        "age": 25
    }
    response = requests.post(f"{BASE_URL}/users/", json=invalid_user_data)
    print(f"Статус: {response.status_code}")
    print(f"Ответ: {response.json()}")
    
    # Попытка создать заказ с несуществующим пользователем
    print("\n2. Создание заказа с несуществующим пользователем...")
    invalid_order_data = {
        "title": "Тестовый заказ",
        "description": "Описание заказа",
        "user": 99999
    }
    response = requests.post(f"{BASE_URL}/orders/", json=invalid_order_data)
    print(f"Статус: {response.status_code}")
    print(f"Ответ: {response.json()}")
    
    # Попытка получить несуществующий ресурс
    print("\n3. Получение несуществующего пользователя...")
    response = requests.get(f"{BASE_URL}/users/99999/")
    print(f"Статус: {response.status_code}")
    print(f"Ответ: {response.json()}")

def main():
    """Основная функция тестирования"""
    print("🚀 Запуск тестирования API T3CodesCommanders")
    print("=" * 50)
    
    try:
        # Тестирование API пользователей
        user_id = test_users_api()
        
        if user_id:
            # Тестирование API заказов
            test_orders_api(user_id)
        
        # Тестирование обработки ошибок
        test_error_handling()
        
        print("\n✅ Тестирование завершено успешно!")
        
    except requests.exceptions.ConnectionError:
        print("❌ Ошибка подключения к серверу. Убедитесь, что сервер запущен на http://localhost:8000")
    except Exception as e:
        print(f"❌ Ошибка во время тестирования: {e}")

if __name__ == "__main__":
    main() 