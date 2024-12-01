from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}



class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(verbose_name='автар', **NULLABLE)
    city = models.CharField(max_length=55, verbose_name='страна', **NULLABLE)
    t_chat_id = models.CharField(max_length=50, verbose_name='телеграмм чат id', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []



