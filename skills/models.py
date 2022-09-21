from django.db import models

# Create your models here.
choices = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    )
class ProgrammingLanguage(models.Model):
    title = models.CharField(max_length=50)
    level = models.CharField(max_length=50, default='Beginner', choices=choices)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Programming Languages'
        ordering = ['level']
class Framework(models.Model):
    title = models.CharField(max_length=50)
    level = models.CharField(max_length=50, default='Beginner', choices=choices)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Frameworks'
        ordering = ['level']

class Tool(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Tools'
        ordering = ['title']