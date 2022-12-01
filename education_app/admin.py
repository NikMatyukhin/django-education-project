"""Модуль admin.py нужен для работы с админкой Django"""

from django.contrib import admin

from .models import Work, Assessment

# Register your models here.
admin.site.register(Work)
admin.site.register(Assessment)
