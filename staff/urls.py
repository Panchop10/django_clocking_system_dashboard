"""Staff URLs."""

# Django
from django.urls import path

# Views
from staff import views

urlpatterns = [
    # Search
    path(
        route='',
        view=views.SearchView.as_view(),
        name='search'
    ),
    # Search
    path(
        route='staff/<int:pk>/',
        view=views.DetailView.as_view(),
        name='detail'
    ),
]
