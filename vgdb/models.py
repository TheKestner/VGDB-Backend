from django.db import models

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=200)
    about = models.CharField(max_length=2000)
    perspective = models.CharField(max_length=50)
    release_date = models.DateField(null=True)
    coverart = models.URLField(max_length=500)
    expansions = models.CharField(max_length=200, blank=True)
    franchise = models.ForeignKey('Franchise', on_delete=models.CASCADE, null=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True)

class Franchise(models.Model):
    title = models.CharField(max_length=200, blank=True)

class Company(models.Model):
    name = models.CharField(max_length=200, blank=True)
    about = models.CharField(max_length=2000, blank=True)

class Platforms(models.Model):
    name = models.CharField(max_length=200, blank=True)

class Screenshots(models.Model):
    image = models.URLField(max_length=500, null=True)

class Genre(models.Model):
    title = models.CharField(max_length=200, blank=True)

class Mode(models.Model):
    name = models.CharField(max_length=200, blank=True)