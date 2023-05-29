from django.urls import path
from . import views
from .views import ProfileView

'app/model_viewtype'

urlpatterns = [
    path('', views.home, name='cookin-home'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('about/', views.RecipeListView.as_view(), name='cookin-about'),
    path('recipe/create/', views.RecipeCreateView.as_view(), name='recipe-create'),
    path('recipe/<int:pk>/update/', views.RecipeUpdateView.as_view(), name='recipe-update'),
    path('recipe/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipe-delete'),
    path('profile/', ProfileView.as_view(), name='profile'),
]