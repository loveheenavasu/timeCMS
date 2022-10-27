from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Departments
# from .permissions import IsManager, IsClient, IsEmployee
from .serializers import DepartmentsSerializer

# Create your views here.
from django.contrib.auth import get_user_model

# Create your views here.
class Departments(generics.CreateAPIView, generics.ListCreateAPIView, generics.RetrieveAPIView):
    # permission_classes = [IsClient, ]
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 200,
            'message': 'Departments successfully created.',
            'data': response.data
        })