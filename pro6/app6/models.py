from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=20)
    department=models.CharField(max_length=15)
    age=models.IntegerField()
    experience=models.IntegerField()