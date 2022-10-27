from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Projects, Task, Remarks, ProgressStatus
# from .permissions import IsManager, IsClient, IsEmployee
from .serializers import ProjectsSerializer, TaskSerializer, ProgressStatusSerializer, RemarksSerializer

# Create your views here.
from django.contrib.auth import get_user_model

# Create your views here.
class Projects(generics.CreateAPIView, generics.ListCreateAPIView, generics.RetrieveAPIView, generics.UpdateAPIView):
    # permission_classes = [IsClient, ]
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 200,
            'message': 'Projects successfully created.',
            'data': response.data
        })

class Task(generics.CreateAPIView, generics.ListCreateAPIView, generics.RetrieveAPIView):
    # permission_classes = [IsClient, ]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 200,
            'message': 'Projects successfully created.',
            'data': response.data
        })

class Remarks(generics.CreateAPIView, generics.ListCreateAPIView, generics.RetrieveAPIView):
    # permission_classes = [IsClient, ]
    queryset = Remarks.objects.all()
    serializer_class = RemarksSerializer
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 200,
            'message': 'Projects successfully created.',
            'data': response.data
        })



class ProgressStatus(generics.CreateAPIView, generics.ListCreateAPIView, generics.RetrieveAPIView, generics.DestroyAPIView, generics.UpdateAPIView):
    # permission_classes = [IsClient, ]
    queryset = ProgressStatus.objects.all()
    serializer_class = ProgressStatusSerializer
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 200,
            'message': 'status successfully created.',
            'data': response.data
        })