import datetime
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit, CompletedHabit
from habits.paginators import HabitPaginator
from users.permissions import UserIsModeratorPermission, UserIsStaffPermission, IsOwnerPermission

from habits.serializers import HabitSerializer, CompletedHabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class MyHabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerPermission | UserIsModeratorPermission]
    pagination_class = HabitPaginator


class PublicHabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    pagination_class = HabitPaginator


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerPermission | UserIsModeratorPermission]


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, UserIsModeratorPermission | IsOwnerPermission]


class HabitDestroyAPIView(generics.DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, UserIsStaffPermission | IsOwnerPermission]


class HabitCompleteCreateAPIView(generics.CreateAPIView):
    serializer_class = CompletedHabitSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        habit = serializer.validated_data.get("habit", None)
        if habit:
            c_habit = CompletedHabit.objects.filter(
                habit_id=habit,
                owner_id=self.request.user).first()
            if c_habit:
                c_habit.completed_at = datetime.datetime.now().astimezone()
                c_habit.save()
            else:
                new_c_habit = serializer.save()
                new_c_habit.owner = self.request.user
                new_c_habit.save()
