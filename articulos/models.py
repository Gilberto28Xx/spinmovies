from distutils.command.upload import upload
from random import choices
from tabnanny import verbose
from tokenize import blank_re
from unicodedata import name
from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    movies_directed = models.CharField(max_length=100, null= True, blank= True)
    
    class Meta:
        verbose_name = "Director"
        verbose_name_plural = "Directors"

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Actors(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta: 
        verbose_name = "Actor"
        verbose_name_plural = "Actors"

    def __str__(self):
        return f"{self.name} {self.last_name}"

class Genero(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Movies(models.Model):
    name = models.CharField(max_length=100)
    year_published = models.IntegerField()
    cathegory = models.CharField(max_length=2, choices=[('M','+Mayor de Edad'),('ME','-Menor de Edad')])
    photo = models.ImageField(upload_to='imgProcess/', null = True, blank = True)
    description = models.CharField(max_length=350, null=True, blank=True)
    directorf = models.ForeignKey(Director, null= True, blank= True, on_delete=models.SET_NULL)
    generof = models.ForeignKey(Genero, null= True,on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return f"{self.name} {self.year_published}"


class Series(models.Model):
    name = models.CharField(max_length=100)
    year_published = models.IntegerField()
    cathegory = models.CharField(max_length=2, choices=[('M','+Mayor de Edad'),('ME','-Menor de Edad')])
    photo = models.ImageField(upload_to='imgProcess/', null = True, blank = True)
    description = models.CharField(max_length=350, null=True, blank=True)
    directorf = models.ForeignKey(Director, null= True, blank= True, on_delete=models.SET_NULL)
    generof = models.ForeignKey(Genero, null= True,on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Serie"
        verbose_name_plural = "Series"

    def __str__(self):
        return f"{self.name} {self.year_published}"

class Documental(models.Model):
    name = models.CharField(max_length=100)
    year_published = models.IntegerField()
    cathegory = models.CharField(max_length=2, choices=[('M','+Mayor de Edad'),('ME','-Menor de Edad')])
    photo = models.ImageField(upload_to='imgProcess/', null = True, blank = True)
    description = models.CharField(max_length=350, null=True, blank=True)
    directorf = models.ForeignKey(Director, null= True, blank= True, on_delete=models.SET_NULL)
    generof = models.ForeignKey(Genero, null= True,on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Documental"
        verbose_name_plural = "Documentales"

    def __str__(self):
        return f"{self.name} {self.year_published}"