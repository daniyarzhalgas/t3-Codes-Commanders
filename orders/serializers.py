from rest_framework import serializers
from .models import Order
from users.models import User
from users.serializers import UserSerializer


class OrderSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Order
    """
    user_detail = UserSerializer(source='user', read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'title', 'description', 'user', 'user_detail', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'user_detail']

    def validate_user(self, value):
        """
        Проверка существования пользователя
        """
        if not User.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Пользователь с указанным ID не существует")
        return value

    def validate_title(self, value):
        """
        Проверка названия заказа
        """
        if not value.strip():
            raise serializers.ValidationError("Название заказа не может быть пустым")
        if len(value) < 3:
            raise serializers.ValidationError("Название заказа должно содержать минимум 3 символа")
        return value

    def validate_description(self, value):
        """
        Проверка описания заказа
        """
        if not value.strip():
            raise serializers.ValidationError("Описание заказа не может быть пустым")
        if len(value) < 10:
            raise serializers.ValidationError("Описание заказа должно содержать минимум 10 символов")
        return value


class OrderUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для обновления заказа
    """
    class Meta:
        model = Order
        fields = ['title', 'description', 'user']

    def validate_user(self, value):
        """
        Проверка существования пользователя при обновлении
        """
        if not User.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Пользователь с указанным ID не существует")
        return value 