from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import TaskView, RemarksView, ProgressStatusView, projects, TimesheetViews, timesheet, ProjectsView
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('<int:id>', views.projects_detail, name='projects'),
    path('projects/<str:id>', ProjectsView.as_view()),
    path('task/', TaskView.as_view()),
    path('remarks/', RemarksView.as_view()),
    path('status/', ProgressStatusView.as_view()),
    path('timesheet/', TimesheetViews.as_view()),
    path('time/', views.timesheet, name='time'),
    path('toggle_screenshot', views.toggle_screenshot_switch, name="toggle_screensort_switch")
]