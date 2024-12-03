from rest_framework import generics

from users.permissions import IsOwnerPermission
from users.models import User
from users.serializers import UserSerializer, UserViewSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import UserIsStaffPermission


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserViewSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserViewSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwnerPermission]


class UserDestroyAPIView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwnerPermission | UserIsStaffPermission]
