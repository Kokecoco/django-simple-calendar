from django.urls import path
from . import views

urlpatters = [
    path('seating', views.seating, name="seating"),
]