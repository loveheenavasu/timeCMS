from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import CreateEmployee, CreateAddress, RoleOperations, CreatePermission

urlpatterns = [
    path('create/', CreateEmployee.as_view()),
    path('address/', CreateAddress.as_view()),
    path('roles/<int:id>/', RoleOperations.as_view()),
    path('permission/', CreatePermission.as_view()),
]