from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import Employee, Address, RoleOperations, Permission

urlpatterns = [
    path('employee/', Employee.as_view()),
    path('address/', Address.as_view()),
    path('roles/<int:id>/', RoleOperations.as_view()),
    path('permission/', Permission.as_view()),
]