from django.db import models


# Model to hold personal information: can therefore be modified through admin
class PersonalInformation(models.Model):
    """Model holding my personal information"""
    bio = models.TextField(max_length=1000)
    email_address = models.EmailField()

    def __str__(self):
        """String for representing the Model object"""
        return "My personal information"


# Model for project to be hosted on the site
class Project(models.Model):
    """Model representing information about an appliction"""
    project_verbose_name = models.CharField(max_length=200)
    project_django_name = models.CharField(max_length=100)
    upload_date = models.DateField()
    description = models.TextField(max_length=1000)

    def __str__(self):
        """String for representing the model option"""
        return f'{self.project_verbose_name} - {self.upload_date}'

    def get_absolute_url(self):
        """Returns the url to access a particular applications"""
        return f'{self.project_django_name}: '


class Webpage(models.Model):
    """Model holding the text to be posted on a given webpage"""
    page_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.page_name}'
