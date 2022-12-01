"""Модуль apps.py нужен для работы с приложением Django"""

from django.apps import AppConfig


class EducationAppConfig(AppConfig):
    """Класс приложения education_app"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "education_app"
