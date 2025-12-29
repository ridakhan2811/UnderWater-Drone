# Admin configurations for all apps
# home/admin.py
from django.contrib import admin
from .models import ProjectInfo

@admin.register(ProjectInfo)
class ProjectInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'team_size', 'created_at']
    fieldsets = (
        ('Project Details', {'fields': ('title', 'tagline', 'description')}),
        ('Statistics', {'fields': ('team_size',)}),
    )
