from django.urls import path
from . import views

'app/model_viewtype'
'recipes/recipes_detail.html'

urlpatterns = [
    path('', views.home, name='cookin-home'),
        path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('about/', views.RecipeListView.as_view(), name='cookin-about'),
]