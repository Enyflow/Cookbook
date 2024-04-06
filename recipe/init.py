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
        {
            'title': 'Tomato Pasta',
            'description': 'Delicious pasta with fresh basil and tomato sauce. '
                           'Cook pasta in boiling salted water until al dente. Meanwhile, '
                           'heat olive oil in a large skillet over medium heat. Add minced '
                           'garlic and cook until fragrant. Stir in diced tomatoes and tomato '
                           'paste, and simmer for 10 minutes. Add cooked pasta to the skillet '
                           'and toss to coat with the sauce. Garnish with fresh basil and grated '
                           'Parmesan cheese before serving.',
            'short_description': 'Simple and delicious tomato pasta.'
        },
        {
            'title': 'Margherita Pizza',
            'description': 'Classic Italian pizza with tomato, mozzarella, and basil. '
                           'Prepare pizza dough by combining flour, yeast, water, and olive oil. '
                           'Roll out the dough into a thin circle and place on a pizza stone. '
                           'Spread tomato sauce over the dough, then add slices of fresh mozzarella '
                           'and cherry tomatoes. Bake in a preheated oven until crust is golden brown. '
                           'Remove from oven and top with fresh basil leaves before serving.',
            'short_description': 'Traditional Margherita pizza with fresh ingredients.'
        },
        {
            'title': 'Caesar Salad',
            'description': 'Crisp salad with Caesar dressing and bread croutons. '
                           'Prepare Caesar dressing by whisking together mayonnaise, minced garlic, '
                           'Dijon mustard, Worcestershire sauce, lemon juice, and grated Parmesan cheese. '
                           'Toss lettuce leaves with the dressing, then add croutons and shaved Parmesan. '
                           'Garnish with anchovy fillets and freshly ground black pepper before serving.',
            'short_description': 'Refreshing Caesar salad with homemade dressing.'
        },
        {
            'title': 'Mushroom Risotto',
            'description': 'Creamy risotto with fresh porcini mushrooms. '
                           'In a large saucepan, sauté chopped onions in butter until translucent. '
                           'Add Arborio rice and cook until lightly toasted. Gradually add chicken broth '
                           'and stir until absorbed. Stir in sliced mushrooms and cook until tender. '
                           'Finish by stirring in grated Parmesan cheese and chopped parsley before serving.',
            'short_description': 'Rich and flavorful mushroom risotto.'
        },
        {
            'title': 'Chicken Curry',
            'description': 'Spicy chicken with a creamy curry sauce. '
                           'Marinate chicken pieces in a mixture of yogurt, lemon juice, and curry powder. '
                           'Sauté diced onions, garlic, and ginger in a skillet until softened. Add marinated '
                           'chicken and cook until browned. Stir in coconut milk, diced tomatoes, and curry paste. '
                           'Simmer until chicken is cooked through and sauce is thickened. Serve over rice and '
                           'garnish with chopped cilantro before serving.',
            'short_description': 'Savory chicken curry with aromatic spices.'
        },
        {
            'title': 'Spaghetti Carbonara',
            'description': 'A classic Roman dish with spaghetti, eggs, pancetta, and cheese. '
                           'Spaghetti Carbonara is one of the most famous and beloved dishes in Italian cuisine. '
                           'Originally created in Rome, this dish is loved for its simplicity and deliciousness. '
                           'Here\'s the complete recipe:\n\n'
                           'Ingredients:\n'
                           '- 400g spaghetti\n'
                           '- 200g pancetta or guanciale\n'
                           '- 3 eggs\n'
                           '- 100g grated Pecorino Romano cheese\n'
                           '- Freshly ground black pepper\n'
                           '- Salt to taste\n\n'
                           'Instructions:\n'
                           '1. In a large pot, bring a generous amount of salted water to a boil. Add the spaghetti '
                           'and cook until al dente according to the package instructions.\n'
                           '2. Meanwhile, cut the pancetta or guanciale into thin strips. In a skillet, fry the '
                           'pancetta or guanciale until crispy and golden brown.\n'
                           '3. In a bowl, beat the eggs and add the grated Pecorino Romano cheese. Mix well.\n'
                           '4. Drain the spaghetti al dente and transfer them to the skillet with the pancetta or '
                           'guanciale, retaining some of the cooking water.\n'
                           '5. Toss the spaghetti with the pancetta or guanciale until evenly coated.\n'
                           '6. Remove the skillet from the heat and slowly pour in the egg and cheese mixture, '
                           'stirring continuously to prevent the eggs from scrambling too quickly.\n'
                           '7. Continue stirring until the sauce becomes creamy and coats the spaghetti. If needed, '
                           'add some of the spaghetti cooking water to achieve the desired consistency.\n'
                           '8. Add plenty of freshly ground black pepper and mix well.\n'
                           '9. Serve the Spaghetti Carbonara hot, garnished with additional grated Pecorino Romano '
                           'cheese and freshly ground black pepper if desired. Enjoy your meal!',
            'short_description': 'A classic Roman dish with spaghetti, eggs, pancetta, and cheese.'
        },
    ]

    for recipe_data in recipes:
        recipe = Recipe.objects.create(
            title=recipe_data['title'],
            description=recipe_data['description'],
            short_description=recipe_data['short_description'],
            author=user
        )
        print(f'Recipe "{recipe.title}" created successfully.')

if __name__ == '__main__':
    delete_all_recipes()
    create_recipes()
