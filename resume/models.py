from django.db import models

# Create your models here.
class Education(models.Model):
    course = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    institution_logo = models.ImageField(upload_to='education/institution_logo', null=True, blank=True)
    institution_url = models.URLField(max_length=200, blank=True, null=True)
    institution_city = models.CharField(max_length=100)
    expected_grad_date = models.DateField(null=True, blank=True)
    date_completed = models.DateField(null=True, blank=True)
    certificate_url = models.URLField(max_length=300, blank=True, null=True)
    related_course_work = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.course

    class Meta:
        verbose_name_plural = 'Education'
        ordering = ['-date_completed', '-expected_grad_date']

