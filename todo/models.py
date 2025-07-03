from django.db import models
from django.utils import timezone


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)  # タイトル.
    completed = models.BooleanField(default=False)  # 完了しているか.
    posted_at = models.DateTimeField(default=timezone.now)  # 登録日.
    due_at = models.DateTimeField(null=True, blank=True)  # 締切.

    def is_overdue(self, dt):
        if self.due_at is None:
            return False
        return self.due_at < dt
