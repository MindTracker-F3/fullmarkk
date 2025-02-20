from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User
#from analysis.models import Analysis 
=======
from django.contrib.auth.models import User 
>>>>>>> 32917af504acf0e0e8023d8f2dc39dd099e0b5d9
from django.core.validators import MinValueValidator
from analysis.models import Analysis

# Create your models here.

class MultiAgent(models.Model):
    multiAgent_id = models.AutoField(primary_key=True )
    an_model = models.ForeignKey(Analysis, on_delete=models.CASCADE , null=True)  # الربط هن
    model_name = models.CharField(max_length=255, default="Unnamed Model")  # اسم النموذج الافتراضي
    photos = models.JSONField(default=list)  # قائمة فارغة للصور
    texts = models.JSONField(default=list)  # قائمة فارغة للنصوص
    videos = models.JSONField(default=list)  # قائمة فارغة للفيديوهات
    cookies = models.JSONField(default=list)  # قائمة فارغة للكوكيز
    web_usage = models.JSONField(default=dict)
<<<<<<< HEAD
   # analysis = models.ForeignKey(Analysis, on_delete=models.CASCADE)
=======


    
>>>>>>> 32917af504acf0e0e8023d8f2dc39dd099e0b5d9
