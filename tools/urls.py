from django.urls import path
from . import views

urlpatterns = [
    path('seating/', views.seating, name="seating"),
]