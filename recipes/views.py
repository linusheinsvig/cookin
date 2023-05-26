from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('<h1>Welcome to Cookin</h1>')


def about(request):
    return HttpResponse('<h1>Cookin is a recipes app for you to view and share your favorite recipes!</h1>')