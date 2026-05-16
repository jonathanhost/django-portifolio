from django.contrib import admin
from .models import Project
# Registers the Project model so projects can be added through the Django admin panel.

admin.site.register(Project)