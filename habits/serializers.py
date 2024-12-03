import datetime
from rest_framework import serializers

from habits.models import Habit, CompletedHabit
from habits.validators import TimeToActionValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [TimeToActionValidator("time_to_action_in_sec")]

    def validate(self, data):
        if data.get("reward", None) and data.get("related_habit", None):
            raise serializers.ValidationError("Нельзя назначить вознаграждение и связанную привычку вместе")
        r_habit = data.get("related_habit", None)
        if r_habit:
            list_habits = [Habit.objects.filter(pk=habit.pk).first() for habit in r_habit]
            habit_status = [h.is_pleasant for h in list_habits]
            if not all(habit_status):
                raise serializers.ValidationError("Нельзя назначить связанную привычку, которая не является приятной")
        if data.get("is_pleasant", None) and (data.get("reward", None) or data.get("related_habit", None)):
            raise serializers.ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки")
        return data


class CompletedHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletedHabit
        fields = '__all__'

    def validate(self, data):
        habit = Habit.objects.filter(pk=data['habit'].pk).first()
        user = self.context["request"].user
        if habit.owner != user:
            raise serializers.ValidationError("Закончить привычку может только ее создатель")
        c_habit = CompletedHabit.objects.filter(habit=data['habit'].pk, owner=user).first()
        if c_habit and (datetime.datetime.now().astimezone() - c_habit.completed_at).days >= 7:
            raise serializers.ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней")
        return data
