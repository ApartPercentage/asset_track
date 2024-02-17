from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ('Video Camera', 'Video Camera'),
    ('Recorder', 'Recorder'),
    ('Magewell', 'Magewell'),
    ('Cable', 'Cable'),
    ('Router', 'Router'),
    ('Hard Disk', 'Hard disk'),
    ('Laptop', 'Laptop'),
    ('Adapter', 'Adapter'),
    ('Battery', 'Battery'),
    ('Projector', 'Projector'),
    ('Tripod', 'Tripod'),
    ('Battery Camera', 'Battery camera'),
    ('Router', 'Router'),
    ('Charger', 'Charger'),
    ('Thumbdrive', 'Thumbdrive'),
    ('Battery Charger', 'Battery charger'),
    ('Cable', 'Cable'),
)

    
class Assets(models.Model):
    name = models.CharField(max_length = 100, null = True)
    category = models.CharField(max_length = 100, choices=CATEGORY, null = True)
    description = models.CharField(max_length=200, null = True)
    serial_number = models.CharField(max_length = 100, null = True)
    note = models.CharField(max_length=200, null = True)
    is_available = models.BooleanField(default=True)
    date_added = models.DateField()

    class Meta:
        verbose_name_plural = 'Store'

    def __str__(self):
        return f'{self.category}-{self.name}'

class BorrowTransaction(models.Model):
    asset = models.ForeignKey(Assets, on_delete=models.CASCADE)
    staff_member = models.ForeignKey(User, on_delete=models.CASCADE)
    date_borrowed = models.DateField()
    date_returned = models.DateField(null=True, blank = True)
    
    def __str__(self):
        return f'{self.staff_member.username}-{self.asset}'