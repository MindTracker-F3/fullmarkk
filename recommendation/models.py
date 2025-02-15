from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.

class Recommendation(models.Model):
    recomID = models.AutoField(primary_key=True)
    description = models.TextField(default="No description available.")  # نص افتراضي
    category = models.CharField(max_length=255, default="General")  # تصنيف افتراضي