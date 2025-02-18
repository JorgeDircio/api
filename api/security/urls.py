from django.urls import path
from .views import Class_Register, Class_Activate

urlpatterns = [
    path('register', Class_Register.as_view()),
    path('activate/<str:token>', Class_Activate.as_view()),
]