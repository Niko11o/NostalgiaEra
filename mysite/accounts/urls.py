from django.urls import path
from .views import UserLoginView, register_view, logout_view

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]