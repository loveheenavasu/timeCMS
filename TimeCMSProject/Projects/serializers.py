from rest_framework.serializers import ModelSerializer
from .models import ProjectsModel, Task, Remarks, ProgressStatus, Timesheet


class ProjectsSerializer(ModelSerializer):
    # permission = DepartmentsSerializer(many=True, read_only=True)
    """user model serializer"""
    class Meta:
        model = ProjectsModel
        fields = "__all__"


class TaskSerializer(ModelSerializer):
    # permission = DepartmentsSerializer(many=True, read_only=True)
    """user model serializer"""
    class Meta:
        model = Task
        fields = "__all__"

class RemarksSerializer(ModelSerializer):
    # permission = DepartmentsSerializer(many=True, read_only=True)
    """user model serializer"""
    class Meta:
        model = Remarks
        fields = "__all__"

class ProgressStatusSerializer(ModelSerializer):
    # permission = DepartmentsSerializer(many=True, read_only=True)
    """user model serializer"""
    class Meta:
        model = ProgressStatus
        fields = "__all__"

class TimesheetSerializer(ModelSerializer):
    # permission = DepartmentsSerializer(many=True, read_only=True)
    """user model serializer"""
    class Meta:
        model = Timesheet
        fields = "__all__"