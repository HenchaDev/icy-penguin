from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    personal_info = models.TextField(blank=True)
    medical_history = models.TextField(blank=True)
    feelings = models.TextField(blank=True)