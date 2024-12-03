from datetime import datetime

from celery import shared_task

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_telegram_notification():
    today = datetime.now().astimezone()
    habits = Habit.objects.filter(time=today)
    for habit in habits:
        message = f"Сегодня пора завершить {habit.action}"
        send_telegram_message(habit.owner.t_chat_id, message)
