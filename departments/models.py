"""Department models."""

# Django
from django.db import models

class Department(models.Model):
    """Department model."""

    id = models.IntegerField(primary_key=True)
    department_name = models.CharField(max_length=255)

    def __str__(self):
        """Return title and username."""
        return '{}: {}'.format(self.id, self.department_name)
