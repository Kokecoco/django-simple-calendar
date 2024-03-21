import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group


class Schedule(models.Model):
    """スケジュール"""
    summary = models.CharField('概要', max_length=50)
    description = models.TextField('詳細な説明', blank=True)
    start_time = models.TimeField('開始時間', default=datetime.time(7, 0, 0))
    end_time = models.TimeField('終了時間', default=datetime.time(7, 0, 0))
    date = models.DateField('日付')
    created_at = models.DateTimeField('作成日', default=timezone.now)
    groups = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.summary
