from django.urls import path
from .views import Class_Register

urlpatterns = [
    path('register', Class_Register.as_view()),
]