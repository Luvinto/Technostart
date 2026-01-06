
from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):
    age = models.CharField(max_length=3, verbose_name='Возраст', blank=True)
    class Meta:
        verbose_name = "Пользователь__"
        verbose_name_plural = 'Пользователь__'

    def __str__(self):
        return self.username

