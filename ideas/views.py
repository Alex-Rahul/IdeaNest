from django.shortcuts import render
from .models import Idea

def idea_list(request):
    ideas = Idea.objects.all()
    return render(request, 'ideas/list.html', {'ideas': ideas})

def idea_detail(request, id):
    idea = Idea.objects.get(pk=id)
    return render(request, 'ideas/detail.html', {'idea': idea})
