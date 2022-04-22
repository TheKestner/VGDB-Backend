from django.db import models

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=200)
    about = models.CharField(max_length=2000)
    perspective = models.CharField(max_length=50)
    release_date = models.DateField(null=True)
    coverart = models.URLField(max_length=500)
    expansions = models.CharField(max_length=200)
    franchise = models.ForeignKey('Franchise', on_delete=models.CASCADE)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)

class Franchise(models.Model):
    title = models.CharField(max_length=200)

class Company(models.Model):
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=2000)