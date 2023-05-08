from django.db import models

# Create your models here.
class sigup(models.Model):
    username=models.CharField(max_length=25)
    password=models.IntegerField()
    