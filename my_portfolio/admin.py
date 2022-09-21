from django.contrib import admin
from .models import Portfolio
# Register your models here.

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title','description','image','url', 'date_completed')
    list_display_links = ('title',)
    search_fields = ('title', 'description')
    list_per_page = 25