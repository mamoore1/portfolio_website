from .forms import CharForm
from .models import CharClass
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .npc_generator import character_generator

def index(request):
    if request.method == 'POST':
        form = CharForm(request.POST)
        if form.is_valid():
            char_class = form.cleaned_data['char_class']
            level = form.cleaned_data['level']
            num_char = form.cleaned_data['num_chars']
            return HttpResponseRedirect('/results/')

    else:
        form = CharForm()

    return render(request, 'npc_generator/index.html', {'form': form})


def results(request):
    char_class = request.POST['char_class']
    char_class = CharClass.objects.get(pk=char_class)
    level = int(request.POST['level'])
    num_char = int(request.POST['num_char'])
    characters = []
    for i in range(num_char):
        character = character_generator(char_class, level)
        characters.append(character)
    return render(request, 'npc_generator/results.html', {'characters': characters})