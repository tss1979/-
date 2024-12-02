from datetime import datetime

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


from habits.models import Habit
from users.models import User


# Create your tests here.
class   HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="mail@mail.ru", password='111')
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            owner=self.user,
            time=datetime.now(),
            action="action1",
            period_in_days=2,
            time_to_action_in_sec=100,
        )

    def test_habit_retrieve(self):
        """Тестирование просмотра одной привычки"""
        url = reverse("habits:habit-one", args=(self.habit.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get("action"), self.habit.action)

    def test_lesson_delete(self):
        """Тестирование удаления привычки"""
        url = reverse("habits:habit-delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_lesson_update(self):
        """Тестирование изменения привычки"""
        url = reverse("habits:habit-update", args=(self.habit.pk,))
        data = {"action": "Walk",}
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.all().count(), 1)
        self.assertEqual(response.json().get("action"), "Walk")

    def test_my_habits_list(self):
        """Тестирование получение всех привычек"""
        url = reverse("habits:my_habits-list")
        response = self.client.get(url)
        result = [
            {
             'id': self.habit.pk,
             'owner': self.user,
             'location': None,
             'time': self.habit.time,
             'action': self.habit.action,
             'is_pleasant': False,
             'is_public': False,
             'period_in_days': self.habit.period_in_days,
             'reward': None,
             'time_to_action_in_sec': self.habit.time_to_action_in_sec,
             'related_habit': None,
            }
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get("count"), 1)
        self.assertEqual(response.json().get("results"), result)

    def test_public_habits_list(self):
        """Тестирование получение всех публичных привычек"""
        url = reverse("habits:public_habits-list")
        response = self.client.get(url)
        result = []
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get("count"), 0)
        self.assertEqual(response.json().get("results"), result)

    def test_habit_create(self):
        """Тестирование создания привычки"""
        url = reverse("habits:habit-create")
        data = {
            "owner": self.user,
            "time": datetime.now(),
            "action": "action",
            "period_in_days": 2,
            "time_to_action_in_sec": 100,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

