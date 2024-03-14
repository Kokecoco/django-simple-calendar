from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic
from .forms import BS4ScheduleForm
from .models import Schedule
from . import mixins
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def delete_event(request, pk):
    event = get_object_or_404(Schedule, id=pk)
    if request.method == 'POST':
        event.delete()
    return redirect('/calendar/')  # 削除後のリダイレクト先

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:login')  # 登録後のリダイレクト先
    else:
        form = UserCreationForm()
    return render(request, 'app/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(to='app:calendar')  # ログイン後のリダイレクト先
    else:
        form = AuthenticationForm()
    return render(request, 'app/login.html', {'form': form})

class MyCalendar(LoginRequiredMixin, mixins.MonthWithScheduleMixin, mixins.MonthCalendarMixin, generic.CreateView):
    """月間カレンダー、週間カレンダー、スケジュール登録画面のある欲張りビュー"""
    login_url = '/login/'
    template_name = 'app/mycalendar.html'
    model = Schedule
    date_field = 'date'
    form_class = BS4ScheduleForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        month_calendar_context = self.get_month_calendar()
        context.update(month_calendar_context)
        return context

    def form_valid(self, form):
        schedule = form.save(commit=False)
        schedule.save()
        return redirect('app:calendar')

class EventDetail(LoginRequiredMixin, generic.DetailView):
    """イベントの詳細を表示するビュー"""
    login_url = '/login/'
    template_name = 'app/schedule_detail.html'
    model = Schedule


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # ここに詳細表示に必要なコンテキストを追加するコードを記述する
        return context