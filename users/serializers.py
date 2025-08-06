from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели User
    """
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'age', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_email(self, value):
        """
        Проверка уникальности email
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Пользователь с таким email уже существует")
        return value

    def validate_age(self, value):
        """
        Проверка возраста
        """
        if value < 1:
            raise serializers.ValidationError("Возраст должен быть больше 0")
        if value > 150:
            raise serializers.ValidationError("Возраст не может быть больше 150")
        return value


class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для обновления пользователя
    """
    class Meta:
        model = User
        fields = ['name', 'email', 'age']

    def validate_email(self, value):
        """
        Проверка уникальности email при обновлении
        """
        instance = self.instance
        if instance and User.objects.filter(email=value).exclude(id=instance.id).exists():
            raise serializers.ValidationError("Пользователь с таким email уже существует")
        return value 