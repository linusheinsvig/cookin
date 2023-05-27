from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from . import models


# Create your views here.


def home(request):
    return render(request, 'recipes/home.html')


class RecipeListView(ListView):
    model = models.Recipe
    template_name = 'recipes/about.html'
    context_object_name = 'recipes'


class RecipeDetailView(DetailView):
    model = models.Recipe


