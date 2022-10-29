from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import ProjectsModel, Task, Remarks, ProgressStatus, Timesheet
# from .permissions import IsManager, IsClient, IsEmployee
from .serializers import ProjectsSerializer, TaskSerializer, ProgressStatusSerializer, RemarksSerializer, TimesheetSerializer
# Create your views here.
from django.contrib.auth import get_user_model

# importing ImageGrab class
from PIL import ImageGrab

# importing random module
import random

# importing time module
import time

# Create your views here.
class ProjectsView(generics.CreateAPIView, generics.ListCreateAPIView, generics.RetrieveAPIView, generics.UpdateAPIView):
    # permission_classes = [IsClient, ]
    queryset = ProjectsModel.objects.all()
    serializer_class = ProjectsSerializer
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 200,
            'message': 'Projects successfully created.',
            'data': response.data
        })

class TimesheetViews(generics.CreateAPIView, generics.ListCreateAPIView, generics.RetrieveAPIView, generics.UpdateAPIView):
    # permission_classes = [IsClient, ]
    queryset = Timesheet.objects.all()
    serializer_class = TimesheetSerializer
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 200,
            'message': 'Timesheet successfully created.',
            'data': response.data
        })

class TaskView(generics.CreateAPIView, generics.ListCreateAPIView, generics.RetrieveAPIView):
    # permission_classes = [IsClient, ]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 200,
            'message': 'Task successfully created.',
            'data': response.data
        })

class RemarksView(generics.CreateAPIView, generics.ListCreateAPIView, generics.RetrieveAPIView):
    # permission_classes = [IsClient, ]
    queryset = Remarks.objects.all()
    serializer_class = RemarksSerializer
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 200,
            'message': 'Remarks successfully created.',
            'data': response.data
        })



class ProgressStatusView(generics.CreateAPIView, generics.ListCreateAPIView, generics.RetrieveAPIView, generics.DestroyAPIView, generics.UpdateAPIView):
    # permission_classes = [IsClient, ]
    queryset = ProgressStatus.objects.all()
    serializer_class = ProgressStatusSerializer
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 200,
            'message': 'Progress Status successfully created.',
            'data': response.data
        })


def projects(request):
    all_projects = ProjectsModel.objects.all()
    context = {'all_projects':all_projects}
    return  render(request, 'projects.html', context)
def projects_detail(request, id):
    projects_detail = ProjectsModel.objects.filter(id=id)
    context = {'projects_detail':projects_detail}
    return  render(request, 'projects.html', context)


def toggle_screenshot_switch(request, id):
    print("req. for toggle screenshot for proj id ", id)
    return HttpResponse("screenshot start")


def screenshot():
    while True:
        random_time = random.randint(1, 5)
        time.sleep(random_time)
        snapshot = ImageGrab.grab()
        file_name = str(time.time()) + ".png"
        snapshot.save(file_name)
    return snapshot


def timesheet(request):
    time = Timesheet.objects.filter(user__username=request.user)
    task = Task.objects.filter(assigned_to__username=request.user)
    print(task,'---------------------------->')
    print(time, '==================================>')
    return render(request, 'projects.html')
