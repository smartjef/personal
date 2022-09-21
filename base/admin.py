from django.contrib import admin
from .models import Review, About, Contact
# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name','image','position', 'date')
    list_display_links = ('name', 'position')
    search_fields = ('name', 'position', 'message')
    list_per_page = 25

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title','description','image')
    list_display_links = ('title',)
    search_fields = ('title', 'description')
    list_per_page = 25

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email', 'message')
    list_display_links = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email', 'message')
    list_per_page = 25


admin.site.site_heade = "Jeff's Admin"