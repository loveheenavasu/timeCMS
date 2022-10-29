from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Users, Address, Permission, Roles
# from .permissions import IsManager, IsClient, IsEmployee
from .serializers import UserSerializer, AddressSerializer, RoleSerializer, PermissionSerializer
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets


class EmployeeOperations(generics.CreateAPIView, generics.ListAPIView, generics.RetrieveAPIView, generics.UpdateAPIView,
                         generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [AllowAny, ]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

    # def create(self, request, *args, **kwargs):
    #     response = super().create(request, *args, **kwargs)
    #     return Response({
    #         'status': 200,
    #         'message': 'Employee successfully created.',
    #         'data': response.data
    #     })


class AddressOperations(generics.CreateAPIView, generics.ListAPIView, generics.RetrieveAPIView, generics.UpdateAPIView,
                         generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    # permission_classes = [IsClient, ]
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 200,
            'message': 'Address successfully created.',
            'data': response.data
        })


class RoleOperations(generics.CreateAPIView, generics.ListAPIView, generics.RetrieveAPIView, generics.UpdateAPIView,
                         generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    # permission_classes = [IsClient, ]
    queryset = Roles.objects.all()
    serializer_class = RoleSerializer
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 200,
            'message': 'Role successfully created.',
            'data': response.data
        })


class PermissionOperations(generics.CreateAPIView, generics.ListAPIView, generics.RetrieveAPIView, generics.UpdateAPIView,
                         generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    # permission_classes = [IsClient, ]
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 200,
            'message': 'Permission successfully created.',
            'data': response.data
        })
