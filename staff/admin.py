"""Department admin classes."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from staff.models import Department, Employee, Timeclock

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

@admin.register(Employee)
class EmployeesAdmin(admin.ModelAdmin):
    """Employees admin."""

    list_display = (
        'id',
        'card_uid',
        'first_name',
        'last_name',
        'last_clock_register',
        'dept_name'
        )

    def dept_name(self, obj):
        return obj.department.department_name

    dept_name.short_description = 'Department Name'

    list_display_links = ('id',)
    list_editable = (
        'first_name',
        'last_name',
        )

    search_fields = (
        'first_name',
        'last_name',
        'department_id',
    )

@admin.register(Timeclock)
class TimeclockAdmin(admin.ModelAdmin):
    """Timeclock admin."""

    list_display = (
        'id',
        'clocking_time',
        'clock_status',
        'employee_data',
        )
    def employee_data(self, obj):
        return\
        str(obj.employee.id)\
         + " - " +\
         obj.employee.first_name\
         + " " +\
         obj.employee.last_name


    employee_data.short_description = 'Employee'

    list_display_links = ('id',)

    search_fields = (
        'clocking_time',
        'employee_id',
    )
