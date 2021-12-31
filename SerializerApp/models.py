from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Singer(models.Model):
    name= models.CharField(max_length=100)
    gender= models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=100)
    singer= models.ForeignKey(Singer , on_delete=models.CASCADE, related_name= 'song')
    duration = models.IntegerField()

    def __str__(self):
        return self.title

class Person(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    city =  models.CharField(max_length=50)