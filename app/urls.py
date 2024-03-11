from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('mycalendar/', views.MyCalendar.as_view(), name='mycalendar'),
    path(
        'mycalendar/<int:year>/<int:month>/<int:day>/', views.MyCalendar.as_view(), name='mycalendar'
    ),
    path(
        'month_with_forms/',
        views.MonthWithFormsCalendar.as_view(), name='month_with_forms'
    ),
    path(
        'month_with_forms/<int:year>/<int:month>/',
        views.MonthWithFormsCalendar.as_view(), name='month_with_forms'
    ),
]
