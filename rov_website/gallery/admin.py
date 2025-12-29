# gallery/admin.py
from django.contrib import admin
from .models import GalleryImage

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured', 'uploaded_at']
    list_filter = ['category', 'featured', 'uploaded_at']
    search_fields = ['title', 'description']
    fieldsets = (
        ('Image Info', {'fields': ('title', 'image')}),
        ('Details', {'fields': ('description', 'category')}),
        ('Settings', {'fields': ('featured',)}),
    )





