from django.db import models

# Create your models here.
class ProgrammingLanguage(models.Model):
    title = models.CharField(max_length=50)
    level = models.CharField(max_length=50)

class Framework(models.Model):
    title = models.CharField(max_length=50)
    level = models.CharField(max_length=50)

class Tools(models.Model):
    title = models.CharField(max_length=50)