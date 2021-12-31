from django.db import models

# Create your models here.
class Student(models.Model):
    class CourseType(models.TextChoices):
        MCA = "Mca"
        MTech = "Mtech"
        MBA = "Mba"
        BTech = "Btech"
    name=models.CharField(max_length=50)
    roll= models.IntegerField()
    city=models.CharField(max_length=50)
    course=models.CharField(choices=CourseType.choices,max_length=50)

    def __str__(self):
        return self.name




