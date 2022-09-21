from django.contrib import admin
from .models import Education
# Register your models here.

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('course','institution','institution_url','institution_city','expected_grad_date','date_completed','certificate_url')
    list_display_links = ('course',)
    search_fields = ('course', 'institution', 'institution_city', 'related_course_work')
    list_per_page = 25