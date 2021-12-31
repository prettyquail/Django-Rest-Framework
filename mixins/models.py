from django.db import models

# Create your models here.
class Employee(models.Model):
    class DepartmentType(models.TextChoices):
        iips = "IIPS"
        iet = "IET"
        ims = "IMS"
        scsits = "SCSITS"
    firstname=models.CharField(max_length=50)
    lastname= models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    department=models.CharField(choices=DepartmentType.choices,max_length=50)

    def __str__(self):
        return self.firstname