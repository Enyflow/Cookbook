from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def home(request):
    recipes = models.Recipe.objects.all()
    context = {
    'recipes': recipes
  }
    return render(request, 'home.html', context)

def about(request):
  return render(request, 'about.html', {'title': 'about page'})





