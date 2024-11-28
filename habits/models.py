from django.db import models

from config import settings
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    location = models.CharField(max_length=255, verbose_name='место', **NULLABLE)
    time = models.DateTimeField(verbose_name='время, до которого выполнить привычку')
    action = models.CharField(max_length=255, verbose_name='действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')
    period_in_days = models.IntegerField(default=1, verbose_name='периодичность выполнения в днях')
    reward = models.CharField(max_length=150, verbose_name='вознаграждение', **NULLABLE)
    time_to_action_in_sec = models.IntegerField(verbose_name='время на выполнение')
    related_habit = models.ManyToManyField('Habit', **NULLABLE, verbose_name='связанная привычка')



