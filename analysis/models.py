from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from recommendation.models import Recommendation
from report.models import Report
from user.models import History




class Analysis(models.Model):
    model_id = models.AutoField(primary_key=True )
    reco = models.ForeignKey(Recommendation, on_delete=models.CASCADE , null=True) # مرتبط بالتوصيات
    rep = models.ForeignKey(Report, on_delete=models.CASCADE, null=True) #مرتبط بالتقارير 
    userHistory = models.ForeignKey( History, on_delete=models.CASCADE , null=True) # مرتبط بسجل تاريخي معين
    analyzedPhoto = models.TextField(default="No photo analyzed.")
    analyzedText = models.TextField(default="No text analyzed.")
    analyzedVideo = models.TextField(default="No video analyzed.")
    analyzedWebUsage = models.TextField(default="No web usage analyzed.")


    def __str__(self):
        return f"Analysis {self.model_id} for Report {self.report.report_id}"
   