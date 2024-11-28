from rest_framework import serializers

from habits.models import Habit
from habits.validators import TimeToActionValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [TimeToActionValidator("time_to_action_in_sec")]



