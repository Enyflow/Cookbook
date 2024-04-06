from django import forms
from django.forms import  FileInput
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'short_description', 'description', 'image']
        widgets = {
            'image': FileInput(attrs={'accept': 'image/*', 'class': 'form-control-file'})
        }

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget = forms.Textarea(attrs={'rows': 10})  
        
