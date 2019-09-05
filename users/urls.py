"""Users URLs."""

# Django
from django.urls import path

# Views
from users import views

urlpatterns = [
    # Managment
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),

    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),
]
