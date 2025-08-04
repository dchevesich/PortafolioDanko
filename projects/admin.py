from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'featured', 'created_date']
    list_filter = ['category', 'featured', 'created_date']
    search_fields = ['name', 'description']
    list_editable = ['featured']
    ordering = ['-featured', 'order', '-created_date']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('name', 'short_description', 'description', 'category', 'featured', 'order')
        }),
        ('Enlaces', {
            'fields': ('github_link', 'demo_link')
        }),
        ('Imágenes y Media', {
            'fields': ('image',)
        }),
        ('Tecnologías y Logros', {
            'fields': ('technologies', 'achievements')
        }),
    )