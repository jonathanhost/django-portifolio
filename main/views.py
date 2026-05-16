from django.shortcuts import render
from .models import Project

def home(request):
    return render(request, 'main/home.html')

def projects(request):
    # Retrieves all projects from the database.
    projects = Project.objects.all()
    # Sends the projects data to the projects.html template.
    return render(request, 'main/projects.html', {
        'projects': projects
    })