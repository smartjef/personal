from django.contrib import admin
from .models import Education, Referees
# Register your models here.

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('course','institution','institution_url','institution_city','expected_grad_date','date_completed','certificate_url')
    list_display_links = ('course',)
    search_fields = ('course', 'institution', 'institution_city', 'related_course_work')
    list_per_page = 25

@admin.register(Referees)
class RefereesAdmin(admin.ModelAdmin):
    list_display = ('name','company','position','email','phone','description')
    list_display_links = ('name',)
    search_fields = ('name', 'company', 'position', 'email', 'phone', 'description')
    list_per_page = 25