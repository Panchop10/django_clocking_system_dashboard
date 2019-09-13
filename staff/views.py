"""Staff views."""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

# Models
from staff.models import Employee, Timeclock

# User modules
from staff.services import get_clocking_information

class SearchView(LoginRequiredMixin, ListView):
    """Returns all employee."""

    template_name = 'staff/search.html'
    model = Employee
    ordering = ('first_name',)
    context_object_name = 'employees'

class DetailView(LoginRequiredMixin, DetailView):
    """Staff detail view."""

    template_name = 'staff/timesheet.html'
    slug_field = 'user'
    slug_url_kwarg = 'user'
    queryset = Employee.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """add employee's records to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['records'] = get_clocking_information(user.id)
        return context
