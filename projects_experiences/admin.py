from django.contrib import admin
from .models import Project, Experience, Referees
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','company','image','description','github_url','live_url', 'date_completed')
    list_display_links = ('title',)
    search_fields = ('title', 'description')
    list_per_page = 25

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position','company','start_date','end_date','description')
    list_display_links = ('position',)
    search_fields = ('position', 'description')
    list_per_page = 25

@admin.register(Referees)
class RefereesAdmin(admin.ModelAdmin):
    list_display = ('name','company','position','email','phone')
    list_display_links = ('name',)
    search_fields = ('name', 'company', 'position', 'email', 'phone')
    list_per_page = 25