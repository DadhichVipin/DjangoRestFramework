from django.urls import path

from . import views

urlpatterns = [
    path('studentapi/', views.student_api, name='api'),
    # path('student_api/<int:pk>', views.student_api, name='api'),
]
