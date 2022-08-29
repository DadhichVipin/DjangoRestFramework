from django.urls import path

from . import views

urlpatterns = [
    # path('api/', views.hello, name='api'),
    path('api/', views.student_api, name='api'),
    path('api/<int:pk>', views.student_api, name='api'),
]
