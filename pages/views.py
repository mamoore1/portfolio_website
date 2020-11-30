from django.shortcuts import render
from .models import PersonalInformation, Project, Webpage


# Home page view: Displays a welcome message, sidebar allows access to other views
def home(request):
    """View function for home page of site"""
    webpage = Webpage.objects.filter(page_name__contains="home")[0]
    context = {
        'webpage': webpage,
    }
    return render(request, 'home.html', context)


# About page view: Displays some information about me
def about(request):
    """View function for about page of site"""
    webpage = PersonalInformation.objects.get(id=1)
    context = {
        'webpage': webpage
    }
    return render(request, 'about.html', context)


# Apps page view: displays a list of the currently available apps
def projects(request):
    """View function for projects page"""
    project_list = Project.objects.all()
    context = {
        'project_list': project_list,
    }
    return render(request, 'projects.html', context)