from django.db import models
from django.core.exceptions import ValidationError
from users.models import User


class Order(models.Model):
    """
    Модель заказа с полями: название, описание, ID пользователя
    """
    title = models.CharField(max_length=200, verbose_name="Название заказа")
    description = models.TextField(verbose_name="Описание заказа")
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name="Пользователь",
        related_name='orders'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ['-created_at']

    def __str__(self):
        return f"Заказ: {self.title} (Пользователь: {self.user.name})"

    def clean(self):
        """
        Проверка существования пользователя
        """
        if self.user_id and not User.objects.filter(id=self.user_id).exists():
            raise ValidationError({'user': 'Пользователь с указанным ID не существует'})

    def save(self, *args, **kwargs):
        """
        Проверка существования пользователя перед сохранением
        """
        self.clean()
        super().save(*args, **kwargs) 