# Generated by Django 5.0.2 on 2024-03-02 09:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_remove_userprofile_bmi_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="cancer_screening",
            field=models.TextField(default="2024-01-01"),
        ),
    ]