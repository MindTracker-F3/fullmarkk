from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import MinValueValidator
from analysis.models import Analysis

# Create your models here.

class MultiAgent(models.Model):
    multiAgent_id = models.AutoField(primary_key=True )
    model_name = models.CharField(max_length=255, default="Unnamed Model")  # اسم النموذج الافتراضي
    photos = models.JSONField(default=list)  # قائمة فارغة للصور
    texts = models.JSONField(default=list)  # قائمة فارغة للنصوص
    videos = models.JSONField(default=list)  # قائمة فارغة للفيديوهات
    cookies = models.JSONField(default=list)  # قائمة فارغة للكوكيز
    web_usage = models.JSONField(default=dict)
    model_id = models.ForeignKey(Analysis, on_delete=models.CASCADE, null=True, blank=True )
   