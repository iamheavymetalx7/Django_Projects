from django.contrib import admin

# Register your models here.

from .models import *
##model name is Job inside models.py
admin.site.register(Job)