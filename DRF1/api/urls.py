from django.urls import path

from . import views

urlpatterns = [
    path('stuinfo/<int:pk>', views.stdent_detail, name='student_detail'),
    path('stuinfo/', views.stdent_list, name='students'),
]
