from django.urls import path
from .views import *

app_name = 'app1'

urlpatterns = [
    path('', index, name="index"),
    path('list', IndexView.as_view(), name='list'),
    path('result/', result, name="result"),
    path('create/', create, name = "create"),
    path('detail/<int:id>', detail, name = "detail"),
    path('update/<int:id>', update, name = "update"),
    path('delete/<int:id>', delete, name = "delete"),
]