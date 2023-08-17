
from django.urls import path

from account import views

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name="login"),
    path('register/', views.UserRegistration.as_view(), name="register"),
    path('profile/', views.UserProfile.as_view(), name="profile"),
]
