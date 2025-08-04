from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    for project in projects:
        if project.technologies:
            project.technologies_list = [tech.strip() for tech in project.technologies.split(',')]
        else:
            project.technologies_list = []
    return render(request, 'index.html', {'projects': projects})