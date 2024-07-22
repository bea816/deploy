from django.urls import path
from .views import *

app_name = 'app1'

urlpatterns = [
    path('', index, name="index"),
]