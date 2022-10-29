from django.db import models
from Departments.models import Departments
from UserManagement.models import Users


PRIORITY = (
    ('Highest', 'Highest'),
    ('Lowest', 'Lowest'),
    ('Medium', 'Medium'),
)

class ProgressStatus(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Create your models here.
class ProjectsModel(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(max_length=255)
    deadline = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(max_length=255, choices=PRIORITY, default='Lowest')
    progress_status = models.ForeignKey(ProgressStatus, on_delete=models.CASCADE)
    is_ongoing = models.BooleanField(default=True)
    is_completed = models.BooleanField(default=False)
    received_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    screensort_switch = models.BooleanField(default=False)



class Task(models.Model):
    name = models.CharField(max_length=1000, null=True, blank=True)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    project = models.ForeignKey(ProjectsModel, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Users, blank=True, null=True, on_delete=models.CASCADE)
    priority = models.CharField(max_length=255, choices=PRIORITY, default='Lowest')
    deadline = models.DateTimeField(null=True, blank=True)
    task_created_by = models.CharField(max_length=255, null=True, blank=True)
    progress_status = models.ForeignKey(ProgressStatus, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Remarks(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(ProjectsModel, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Timesheet(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    project = models.ForeignKey(ProjectsModel, on_delete=models.CASCADE, null=True, blank=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)
