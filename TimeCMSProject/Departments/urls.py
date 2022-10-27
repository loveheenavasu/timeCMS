from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import Departments

urlpatterns = [
    path('departments/', Departments.as_view()),
]