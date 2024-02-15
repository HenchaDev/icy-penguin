from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=10)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    bmi = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    vaccination_history = models.TextField()
    previous_medications = models.TextField()
    procedures = models.TextField()
    hospitalizations = models.TextField()
    current_symptoms = models.TextField()
    
    