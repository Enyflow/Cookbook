from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin,PermissionRequiredMixin
from . import models
from .models import Recipe
from .forms import RecipeForm
from django.conf import settings


# Create your views here.



def about(request):
  return render(request, 'about.html', {'title': 'about page'})

class RecipeListView(ListView):
    model = Recipe
    template_name = 'home.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        return Recipe.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = models.Recipe
    template_name = 'recipe_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['default_image_url'] = settings.STATIC_URL + 'images/nr-logo.png'  # URL dell'immagine di default
        return context

class RecipeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('homepage')
    template_name = 'confirm_delete.html'
    permission_required = 'app.delete_recipe'

    def test_func(self):
        recipe = self.get_object()
        user = self.request.user
        return user == recipe.author or user.is_staff

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = models.Recipe
    form_class = RecipeForm  # Utilizza la classe del form personalizzato
    template_name = 'recipe_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        if 'image' not in self.request.FILES:
            # Se l'utente non ha caricato un'immagine, assegna un'immagine predefinita
            form.instance.image = settings.DEFAULT_RECIPE_IMAGE  # Assumi che DEFAULT_RECIPE_IMAGE sia il percorso dell'immagine predefinita
        return super().form_valid(form)
  

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Recipe
    fields = ['title', 'short_description', 'description', 'image']
    template_name = 'recipe_form.html'

    def test_func(self):
        recipe = self.get_object()
        user = self.request.user
        return user == recipe.author or user.is_staff

def search_view(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            results = Recipe.objects.filter(title__icontains=query)
            
        else:
            results = Recipe.objects.none()
        return render(request, 'search_results.html', {'results': results, 'query': query})
