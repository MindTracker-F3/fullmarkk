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

    def _str_(self):
        return self.name
    
    