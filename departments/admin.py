"""Department admin classes."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from departments.models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """Department admin."""

    list_display = ('id', 'department_name')
    list_display_links = ('id',)
    list_editable = ('department_name',)

    search_fields = (
        'id',
        'department_name',
    )
