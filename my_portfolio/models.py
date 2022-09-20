from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/', null=True, blank=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    date_completed = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Portfolio'
        ordering = ['-date_completed']