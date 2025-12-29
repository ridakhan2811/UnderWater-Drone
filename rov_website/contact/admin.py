# contact/admin.py
from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'replied']
    list_filter = ['replied', 'created_at']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['created_at', 'name', 'email', 'phone', 'subject', 'message']
    
    fieldsets = (
        ('Sender Info', {'fields': ('name', 'email', 'phone')}),
        ('Message', {'fields': ('subject', 'message')}),
        ('Status', {'fields': ('replied', 'created_at')}),
    )
    
    def has_add_permission(self, request):
        return False