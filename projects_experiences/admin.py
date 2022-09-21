from django.contrib import admin
from .models import Project, Experience
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','company','description','github_url','live_url', 'date_completed')
    list_display_links = ('title',)
    search_fields = ('title', 'description')
    list_per_page = 25

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position','company','start_date','end_date','description')
    list_display_links = ('position',)
    search_fields = ('position', 'description')
    list_per_page = 25