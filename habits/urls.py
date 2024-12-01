from rest_framework.routers import DefaultRouter
from django.urls import path


from habits.apps import HabitsConfig
from habits.models import CompletedHabit
from habits.views import MyHabitListAPIView, PublicHabitListAPIView, HabitRetrieveAPIView, HabitCreateAPIView, \
    HabitUpdateAPIView, HabitDestroyAPIView, HabitCompleteCreateAPIView

app_name = HabitsConfig.name


urlpatterns = [
    path('my_habits/', MyHabitListAPIView.as_view(), name='my_habits-list'),
    path('habits/', PublicHabitListAPIView.as_view(), name='public_habits-list'),
    path('habits/<int:pk>', HabitRetrieveAPIView.as_view(), name='habit-one'),
    path('habits/create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('habits/complete/', HabitCompleteCreateAPIView.as_view(), name='habit-complete'),
    path('habits/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit-update'),
    path('habits/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit-delete'),
]
