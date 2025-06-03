from django.contrib import admin
from .models import Student, Result  # Import your models here

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'enrollment_date')
    search_fields = ('name', 'email')

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'score', 'date_recorded')
    list_filter = ('subject',)
    search_fields = ('student__name',)
