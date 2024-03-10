from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=10)
    ethnicity_race = models.CharField(max_length=100, blank=True)
    socioeconomic_status = models.CharField(max_length=100, blank=True)
    family_history_chronic_diseases = models.TextField(blank=True)
    diagnosed_chronic_conditions = models.TextField(blank=True)
    medications = models.TextField(blank=True)
    surgeries = models.TextField(blank=True)
    typical_daily_diet = models.CharField(max_length=50, blank=True)
    physical_activity_frequency = models.CharField(max_length=50, blank=True)
    smoking_habits = models.CharField(max_length=100, blank=True)
    alcohol_consumption = models.CharField(max_length=100, blank=True)
    recreational_drug_use = models.CharField(max_length=100, blank=True)
    stress_management_methods = models.CharField(max_length=100, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    blood_pressure = models.CharField(max_length=20, blank=True)
    cholesterol_levels = models.CharField(max_length=20, blank=True)
    blood_glucose_levels = models.CharField(max_length=20, blank=True)
    air_pollution_exposure = models.BooleanField(default=False)
    occupational_hazards = models.BooleanField(default=False)
    clean_drinking_water_access = models.BooleanField(default=True)
    genetic_conditions = models.TextField(blank=True)
    genetic_testing_results = models.TextField(blank=True)
    medical_compliance = models.CharField(max_length=20, blank=True)
    health_literacy = models.CharField(max_length=20, default='Moderate')
    mental_health_diagnosis = models.TextField(blank=True)
    social_support_network = models.TextField(blank=True)
    occupation = models.CharField(max_length=100, blank=True)
    work_stress = models.TextField(blank=True)
    last_checkup = models.DateField(null=True, blank=True)  # Changed default value to null
    cancer_screening = models.TextField(blank=True)
    residential_area = models.CharField(max_length=100, blank=True)
    access_to_healthcare = models.BooleanField(default=True)
    additional_comments = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.user.username
