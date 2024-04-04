import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from recipe.models import Recipe
from django.contrib.auth.models import User

def delete_all_recipes():
    Recipe.objects.all().delete()
    print("All recipes deleted successfully.")

def create_recipes():
    user = User.objects.first()  # Assuming there's at least one user in the database
    recipes = [
        {'title': 'Tomato Pasta', 'description': 'Delicious pasta with fresh basil and tomato sauce.'},
        {'title': 'Margherita Pizza', 'description': 'Classic Italian pizza with tomato, mozzarella, and basil.'},
        {'title': 'Caesar Salad', 'description': 'Crisp salad with Caesar dressing and bread croutons.'},
        {'title': 'Mushroom Risotto', 'description': 'Creamy risotto with fresh porcini mushrooms.'},
        {'title': 'Chicken Curry', 'description': 'Spicy chicken with a creamy curry sauce.'},
    ]

    for recipe_data in recipes:
        recipe = Recipe.objects.create(
            title=recipe_data['title'],
            description=recipe_data['description'],
            author=user
        )
        print(f'Recipe "{recipe.title}" created successfully.')

if __name__ == '__main__':
    delete_all_recipes()
    create_recipes()
