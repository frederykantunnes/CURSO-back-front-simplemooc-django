from django.contrib import admin
from .models import Courses
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'create_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Courses, CourseAdmin)