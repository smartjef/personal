from turtle import position
from django.db import models

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='reviews/', null=True, blank=True)
    position = models.CharField(max_length=50)
    message = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Reviews'
        ordering = ['-date']

class About(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='about/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'About'

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Contact'

