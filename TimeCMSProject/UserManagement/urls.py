from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import EmployeeOperations, AddressOperations, RoleOperations, PermissionOperations

urlpatterns = [
    path('employee/<int:id>/', EmployeeOperations.as_view()),
    path('address/', AddressOperations.as_view()),
    path('roles/<int:id>/', RoleOperations.as_view()),
    path('permission/<int:id>', PermissionOperations.as_view()),
]