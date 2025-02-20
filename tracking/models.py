from django.db import models
from django.utils.timezone import now

class UserActivity(models.Model):
    url = models.CharField(max_length=500)
    timestamp = models.DateTimeField(default=now)
    clicks = models.IntegerField(default=0)
    session_time = models.FloatField(default=0.0, null=True)  # السماح بالقيم الفارغة
    text = models.TextField(blank=True, null=True)
    images = models.JSONField(default=list, blank=True)
    videos = models.JSONField(default=list, blank=True)

    def __str__(self):
        return f"{self.url} - {self.timestamp}"


