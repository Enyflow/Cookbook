from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

def get_default_image():
    return 'recipe.png'

# Create your models here.
class Recipe(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  short_description = models.CharField(max_length=200,default='')
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='recipe_images/',null=True, blank=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  

  def get_absolute_url(self):
      return reverse("detail", kwargs={"pk": self.pk})


  def __str__(self):
    return self.title
  
class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0, choices=((1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')))

    def __str__(self):
        return self.text