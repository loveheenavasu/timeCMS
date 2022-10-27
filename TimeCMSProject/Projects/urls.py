from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import Projects, Task, Remarks, ProgressStatus

urlpatterns = [
    path('projects/<str:id>', Projects.as_view()),
    path('task/', Task.as_view()),
    path('remarks/', Remarks.as_view()),
    path('status/', ProgressStatus.as_view()),
]