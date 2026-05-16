from django.urls import path
from . import views

# URL patterns for the main application.
urlpatterns = [
     # Home page route.
    path('', views.home, name='home'),
     # Projects page route.
    path('projects/', views.projects, name='projects'),
]