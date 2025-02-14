from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
#from multiagent.models import MultiAgent
# Create your models here.

class Report(models.Model):
    report_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   # multiagent = models.ForeignKey(MultiAgent, on_delete=models.CASCADE , null=True, blank=True)
    total_usage_hours = models.FloatField(default=0.0, validators=[MinValueValidator(0.0)])  # الاستخدام الافتراضي 0 ساعة
    web_usage_data = models.JSONField(default=dict)  # بيانات افتراضية كقاموس فارغ
    number_of_clicks_web = models.IntegerField(default=0, validators=[MinValueValidator(0)])  # الافتراضي 0 نقرة
    total_clicks = models.IntegerField(default=0, validators=[MinValueValidator(0)])  # الافتراضي 0 نقرة