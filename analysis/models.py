from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
#from multiagent.models import MultiAgent

class Analysis(models.Model):
    model_id = models.AutoField(primary_key=True )
    analyzedPhoto = models.TextField(default="No photo analyzed.")
    analyzedText = models.TextField(default="No text analyzed.")
    analyzedVideo = models.TextField(default="No video analyzed.")
    analyzedWebUsage = models.TextField(default="No web usage analyzed.")
    #multiAgent_id = models.ForeignKey(MultiAgent, on_delete=models.CASCADE, null=True, blank=True )
