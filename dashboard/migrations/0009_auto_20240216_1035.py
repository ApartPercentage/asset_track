# Generated by Django 3.0.14 on 2024-02-16 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_assets_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowtransaction',
            name='date_borrowed',
            field=models.DateField(),
        ),
    ]