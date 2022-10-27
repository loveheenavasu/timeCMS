from rest_framework.serializers import ModelSerializer
from .models import Users, Address, Roles, Permission

class UserSerializer(ModelSerializer):
    """user model serializer"""
    class Meta:
        model = Users
        fields = "__all__"

class AddressSerializer(ModelSerializer):
    """user model serializer"""
    class Meta:
        model =Address
        fields = "__all__"

class PermissionSerializer(ModelSerializer):
    """user model serializer"""
    class Meta:
        model = Permission
        fields = "__all__"


class RoleSerializer(ModelSerializer):
    permission = PermissionSerializer(many=True, read_only=True)
    """user model serializer"""
    class Meta:
        model = Roles
        fields = "__all__"

