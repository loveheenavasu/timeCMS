from rest_framework.serializers import ModelSerializer
from .models import Departments


class DepartmentsSerializer(ModelSerializer):
    # permission = DepartmentsSerializer(many=True, read_only=True)
    """user model serializer"""
    class Meta:
        model = Departments
        fields = "__all__"