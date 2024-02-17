# Generated by Django 3.0.14 on 2024-02-14 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_remove_assets_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='category',
            field=models.CharField(choices=[('Video Camera', 'Video Camera'), ('Recorder', 'Recorder'), ('Magewell', 'Magewell'), ('Cable', 'Cable'), ('Router', 'Router'), ('Hard Disk', 'Hard disk'), ('Laptop', 'Laptop'), ('Adapter', 'Adapter'), ('Battery', 'Battery'), ('Projector', 'Projector'), ('Tripod', 'Tripod'), ('Battery Camera', 'Battery camera'), ('Router', 'Router'), ('Charger', 'Charger'), ('Thumbdrive', 'Thumbdrive'), ('Battery Charger', 'Battery charger'), ('Cable', 'Cable')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='borrowtransaction',
            name='date_borrowed',
            field=models.DateField(auto_now=True),
        ),
    ]
