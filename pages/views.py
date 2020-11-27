from django.shortcuts import render


# Home page view: Displays a welcome message, sidebar allows access to other views
def home(request):
    """View function for home page of site"""
    return render(request, 'home.html')

# About page view: Displays some information about me
def about(request):
    """View function for about page of site"""
    return render(request, 'about.html')

# Apps page view: displays a list of the currently available apps
def apps(request):
    """View function for applications page"""
    return render(request, 'about.html')