from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cookin-home'),
    path('about/', views.about, name='cookin-about'),
]