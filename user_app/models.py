from django.db import models

# Create your models here.
class Temp(models.Model):
    name = models.CharField(max_length=10)
