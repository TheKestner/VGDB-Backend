from django.db import models

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=200)
    about = models.CharField(max_length=2000)
    perspective = models.CharField(max_length=50)
    release_date = models.DateField(null=True)
    coverart = models.URLField(max_length=500)
    expansions = models.CharField(max_length=200, blank=True)
    franchise = models.ForeignKey('Franchise', on_delete=models.CASCADE, blank=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True)
    platforms = models.ManyToManyField('Platform', blank=True)
    screenshot = models.ManyToManyField('Screenshot', blank=True)
    genre = models.ManyToManyField('Genre', blank=True)
    mode = models.ManyToManyField('Mode', blank=True)

    def __str__(self):
        return self.title


class Franchise(models.Model):
    title = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

class Company(models.Model):
    name = models.CharField(max_length=200, blank=True)
    about = models.CharField(max_length=2000, blank=True)

    def __str__(self):
        return self.name

class Platform(models.Model):
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class Screenshot(models.Model):
    image = models.URLField(max_length=500, null=True)

class Genre(models.Model):
    title = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

class Mode(models.Model):
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name