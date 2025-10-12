
from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):
    # Удаляем дублирующиеся поля username, password, email
    # AbstractUser уже содержит их и методы аутентификации
    age = models.CharField(max_length=3, verbose_name='Возраст', blank=True) # Рекомендуется сделать необязательным

    class Meta:
        verbose_name = "Пользователь__"
        verbose_name_plural = 'Пользователь__'

    def __str__(self):
        # Опционально: добавьте строковое представление
        return self.username

