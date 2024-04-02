# Generated by Django 5.0.2 on 2024-03-02 16:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0009_alter_userprofile_air_pollution_exposure_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="additional_comments",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="alcohol_consumption",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="blood_glucose_levels",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="blood_pressure",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="cancer_screening",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="cholesterol_levels",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="diagnosed_chronic_conditions",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="ethnicity_race",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="family_history_chronic_diseases",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="genetic_conditions",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="genetic_testing_results",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="last_checkup",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="medical_compliance",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="medications",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="mental_health_diagnosis",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="occupation",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="physical_activity_frequency",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="recreational_drug_use",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="residential_area",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="smoking_habits",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="social_support_network",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="socioeconomic_status",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="stress_management_methods",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="surgeries",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="typical_daily_diet",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="work_stress",
            field=models.TextField(blank=True),
        ),
    ]