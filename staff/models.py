"""Staff models."""

# Django
from django.db import models

class Department(models.Model):
    """Department model."""

    id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=255)

    def __str__(self):
        """Return title and department name."""
        return '{}: {}'.format(self.id, self.department_name)

class Employee(models.Model):
    """Employee model."""

    id = models.AutoField(primary_key=True)
    card_uid = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    working = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_clock_register = models.DateTimeField(default=None)

    def __str__(self):
        """Return id and name."""
        return '{}: {} {}'.format(self.id, self.first_name, self.last_name)

class Timeclock(models.Model):
    """Timeclock model."""

    id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    sent = models.IntegerField()
    clocking_time = models.DateTimeField(default=None)
    clock_status = models.IntegerField()

    def __str__(self):
        """Return employee and clocking time."""
        return '{} {}: {}'.format(\
            self.id,\
            self.employee,\
            self.clocking_time\
        )
