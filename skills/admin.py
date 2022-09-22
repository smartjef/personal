from django.contrib import admin
from .models import ProgrammingLanguage, Framework, Tool
# Register your models here.

@admin.register(ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ('title','level')
    list_display_links = ('title',)
    search_fields = ('title', 'level')
    list_per_page = 25


@admin.register(Framework)
class FrameworkAdmin(admin.ModelAdmin):
    list_display = ('title','level')
    list_display_links = ('title',)
    search_fields = ('title', 'level')
    list_per_page = 25

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)
    list_per_page = 25