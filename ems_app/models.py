from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    joinDate = models.DateField()
    birthDate = models.DateField()
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    salary = models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)