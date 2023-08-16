
from django.urls import path

from account import views

urlpatterns = [
    path('register/', views.UserRegistration.as_view(), name="register"),
]
