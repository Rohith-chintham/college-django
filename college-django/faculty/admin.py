from django.contrib import admin
from .models import Faculty, Course

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department')
    search_fields = ('name', 'email', 'department')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'faculty', 'credits')
    list_filter = ('credits',)
    search_fields = ('title', 'faculty__name')
