# Generated by Django 5.0.2 on 2024-03-02 09:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="bmi",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="current_symptoms",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="hospitalizations",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="previous_medications",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="procedures",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="vaccination_history",
        ),
        migrations.AddField(
            model_name="userprofile",
            name="access_to_healthcare",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="additional_comments",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="air_pollution_exposure",
            field=models.TextField(default=False),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="alcohol_consumption",
            field=models.CharField(default="None", max_length=100),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="blood_glucose_levels",
            field=models.CharField(default="None", max_length=20),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="blood_pressure",
            field=models.CharField(default="None", max_length=20),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="cancer_screening",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="cholesterol_levels",
            field=models.CharField(default="None", max_length=20),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="clean_drinking_water_access",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="diagnosed_chronic_conditions",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="ethnicity_race",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="family_history_chronic_diseases",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="genetic_conditions",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="genetic_testing_results",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="health_literacy",
            field=models.CharField(default="Moderate", max_length=20),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="last_checkup",
            field=models.DateField(default="1970-01-01"),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="medical_compliance",
            field=models.CharField(default="", max_length=20),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="medications",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="mental_health_diagnosis",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="occupation",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="occupational_hazards",
            field=models.TextField(default=False),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="physical_activity_frequency",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="recreational_drug_use",
            field=models.CharField(default="None", max_length=100),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="residential_area",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="smoking_habits",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="social_support_network",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="socioeconomic_status",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="stress_management_methods",
            field=models.CharField(default="None", max_length=100),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="surgeries",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="typical_daily_diet",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="work_stress",
            field=models.TextField(default=""),
        ),
    ]
