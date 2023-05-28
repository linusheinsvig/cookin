from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
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


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = models.Recipe
    fields = ['title', 'ingrediens']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Recipe
    fields = ['title', 'ingrediens']

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('cookin-home')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author


class ProfileView(LoginRequiredMixin, ListView):
    model = models.Recipe
    template_name = 'users/profile.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)
