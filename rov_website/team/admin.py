# team/admin.py
from django.contrib import admin
from .models import TeamMember

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'subdivision', 'order']
    list_filter = ['role', 'subdivision']
    search_fields = ['name', 'email']
    fieldsets = (
        ('Personal Info', {'fields': ('name', 'image', 'role', 'subdivision')}),
        ('Contact', {'fields': ('email', 'phone')}),
        ('Bio', {'fields': ('bio',)}),
        ('Social Links', {'fields': ('linkedin', 'github')}),
        ('Ordering', {'fields': ('order',)}),
    )

