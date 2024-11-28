from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.paginators import HabitPaginator
from users.permissions import IsOwnerPermission
from users.permissions import UserIsModeratorPermission, UserIsStaffPermission

from school.serializers import CourseSerializer, LessonSerializer
class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerPermission | UserIsModeratorPermission]
    pagination_class = SchoolPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerPermission | UserIsModeratorPermission]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, UserIsModeratorPermission | IsOwnerPermission]


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, UserIsStaffPermission | IsOwnerPermission]

