from django.shortcuts import render, HttpResponse

recipes = [{
    'author': 'Linus',
    'title': 'Arrabiata',
    'ingrediens': 'Pasta, Tomato, Garlic',
    'date_posted': '26 May, 2023'
},
{
    'author': 'Linus',
    'title': 'Carbonara',
    'ingrediens': 'Pasta, Tomato, Garlic',
    'date_posted': '18 May, 2023'
},
{
    'author': 'Linus',
    'title': 'Pizza',
    'ingrediens': 'Pasta, Tomato, Garlic',
    'date_posted': '20 May, 2023'
}
]

# Create your views here.


def home(request):
    context = {
        'recipes': recipes
    }
    return render(request, 'recipes/home.html', context)


def about(request):
    return render(request, 'recipes/about.html')
