from django.db import models

# Create your models here.
class employee(models.Model):
    emp_id=models.IntegerField()
    emp_name=models.CharField(max_length=25)
    # gender=models.CharField(max_length=10)
    place=models.CharField(max_length=25)
    company_name=models.CharField(max_length=25)
    designation=models.CharField(max_length=25)
    salary=models.IntegerField()