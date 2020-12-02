from django.urls import path, re_path

from . import views

app_name = 'npc_generator'
urlpatterns = [
    path('', views.index, name='index'),
    path('results', views.results, name='results')
]