from rest_framework.routers import DefaultRouter
from django.urls import path


from habits.apps import HabitsConfig

app_name = HabitsConfig.name


urlpatterns = [
    path('habits/', HabitsListAPIView.as_view(), name='habits-list'),

]
