from django.contrib import admin
from .models import Assets, BorrowTransaction

# Register your models here.
admin.site.register(Assets)
admin.site.register(BorrowTransaction)
