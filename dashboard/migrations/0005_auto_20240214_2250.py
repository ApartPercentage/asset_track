# Generated by Django 3.0.14 on 2024-02-14 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20240214_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='category',
            field=models.CharField(choices=[('Video Camera', 'Video Camera'), ('recorder', 'Recorder'), ('magewell', 'Magewell'), ('cable', 'Cable'), ('router', 'Router'), ('hard disk', 'Hard disk'), ('laptop', 'Laptop'), ('adapter', 'Adapter'), ('battery', 'Battery'), ('projector', 'Projector'), ('tripod', 'Tripod'), ('battery camera', 'Battery camera'), ('router', 'Router'), ('charger', 'Charger'), ('thumbdrive', 'Thumbdrive'), ('battery charger', 'Battery charger'), ('cable', 'Cable')], max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]