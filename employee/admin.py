from django.contrib import admin

from . import models
# Register your models here.

@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = [
        'department'
    ]
    
    
@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        'fname',
        'lname',
        'department',
        'education',
        'age',
    ]