# Generated by Django 3.0.14 on 2024-02-16 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20240214_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='assets',
            name='date_added',
            field=models.DateField(auto_now=True),
        ),
    ]
