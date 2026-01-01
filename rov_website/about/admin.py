# about/admin.py
from django.contrib import admin
from .models import Vehicle, Subdivision 

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'order']
    list_filter = ['year']
    fieldsets = (
        ('Vehicle Info', {'fields': ('name', 'year', 'image')}),
        ('Details', {'fields': ('description', 'features')}),
        ('Ordering', {'fields': ('order',)}),
    )

@admin.register(Subdivision)
class SubdivisionAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon']
    fields = ['name', 'description', 'icon']


