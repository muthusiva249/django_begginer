from django.db import models

# Create your models here.
class Employee(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    designation = models.CharField(max_length=20,default='trainee')
    salary = models.FloatField(max_length=15,default=10)


class Meta:
    db_table = "Employee"