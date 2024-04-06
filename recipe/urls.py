"""
URL configuration for cookbook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .init import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.RecipeListView.as_view(), name="homepage"),
    path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name="detail"),
    path('recipe/create', views.RecipeCreateView.as_view(), name="create"),
    path('recipe/<int:pk>/update', views.RecipeUpdateView.as_view(), name="update"),
    path('recipe/<int:pk>/delete', views.RecipeDeleteView.as_view(), name="delete"),
    path('recipe/<int:recipe_id>/rate/', views.rate_recipe, name='rate_recipe'),
    path('recipe/<int:recipe_id>/comment/', views.add_comment, name='add_comment'),
    path('about/', views.about, name='about'),
    path('search/', views.search_view, name='search'),
]


#delete_all_recipes()
#create_recipes()
