from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator


class User(models.Model):
    """
    Модель пользователя с полями: имя, email, возраст
    """
    name = models.CharField(max_length=100, verbose_name="Имя пользователя")
    email = models.EmailField(
        unique=True, 
        verbose_name="Email",
        validators=[EmailValidator()]
    )
    age = models.PositiveIntegerField(
        verbose_name="Возраст",
        validators=[
            MinValueValidator(1, message="Возраст должен быть больше 0"),
            MaxValueValidator(150, message="Возраст не может быть больше 150")
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.email})"

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.age and self.age < 1:
            raise ValidationError({'age': 'Возраст должен быть положительным числом'}) 