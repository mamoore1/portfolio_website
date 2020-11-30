from django.contrib import admin
from .models import PersonalInformation, Project, Webpage

admin.site.register(PersonalInformation)
admin.site.register(Project)
admin.site.register(Webpage)
