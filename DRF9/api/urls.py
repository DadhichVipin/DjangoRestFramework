from django.urls import path

from . import views

urlpatterns = [
    path('api/', views.StudentAPI.as_view(), name='api'),
    path('api/<int:pk>', views.StudentAPI.as_view(), name='api_stu'),
]
