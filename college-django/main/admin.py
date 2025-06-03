from django.contrib import admin
from .models import ContactMessage  # Replace with your actual model names

# Example admin registration
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')  # Fields to show in admin list view
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
