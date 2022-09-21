from django.db import models

# Create your models here.
class Experience(models.Model):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name_plural = 'Experience'
        ordering = ['-end_date', '-start_date']
    
class Project(models.Model):
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    description = models.TextField()
    github_url = models.URLField(max_length=200, blank=True, null=True)
    live_url = models.URLField(max_length=200, blank=True, null=True)
    date_completed = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Projects'
        ordering = ['-date_completed']
