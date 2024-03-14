from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path(
        '', views.MyCalendar.as_view(), name='calendar'
    ),
    path('calendar/', views.MyCalendar.as_view(), name='calendar'),
    path(
        'calendar/<int:year>/<int:month>/<int:day>/', views.MyCalendar.as_view(), name='calendar'
    ),
    path(
        'calendar/<int:year>/<int:month>', views.MyCalendar.as_view(), name='calendar'
    ),
    path(
        'event_detail/<int:pk>/',
        views.EventDetail.as_view(), name='event_detail'
    ),
    path('login/', views.login_view, name='login'),
    path('delete/<int:pk>/', views.delete_event, name='delete'),
    path('signup/', views.signup_view, name="signup"),
]
