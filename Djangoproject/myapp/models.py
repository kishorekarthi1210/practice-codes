from django.db import models

# Create your models here.
class ObjectMaster(models.Model):
    Firstname = models.CharField(max_length=20,default="")
    Lastname=models.CharField(max_length=20,default="")
    Email=models.CharField(max_length=30,default="")
    password=models.CharField(max_length=15,default="")
    EmployeeId=models.ForeignKey
