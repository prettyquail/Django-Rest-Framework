from django.db import models

# Create your models here.


class Customer(models.Model):
    firstname=models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    address=models.TextField()
    city=models.CharField(max_length=50)

    def __str__(self):
        return self.firstname




