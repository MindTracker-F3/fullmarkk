from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class CustomUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default="Unnamed User")
    age = models.IntegerField(validators=[MinValueValidator(1)], null=True, blank=True)  
    gender = models.CharField(max_length=10, default="Not Specified")  
    email = models.EmailField(unique=True, default="example@example.com")
    password = models.CharField(max_length=255, default="password123")

    def __str__(self):
        return self.name
    
class History(models.Model):
    userHistory = models.OneToOneField(CustomUser, on_delete=models.CASCADE , related_name="histories" , primary_key=True ) # لتسهيل جلب جميع سجلات History للمستخدم بسهولة
    condition_name = models.JSONField(default=list)  # قائمة فارغة كقيمة افتراضية
    diagnosis_date = models.DateField(auto_now_add=True)  # يتم تعيين التاريخ تلقائيًا
    current_status = models.CharField(max_length=255, default="Unknown") # الحالة الافتراضية


    def __str__(self):
        return f"History of {self.user.username} - {self.condition_name}"