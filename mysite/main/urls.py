from django.contrib import admin
from django.urls import path
from django.conf import settings


from .views import index

app_name = 'main'

urlpatterns = [
    path('', index),

]
