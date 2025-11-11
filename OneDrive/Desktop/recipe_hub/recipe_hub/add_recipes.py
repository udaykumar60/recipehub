import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_hub.settings')
django.setup()

from recipes.models import Recipe
import json

recipes_data = [
    {
        'title': 'Spaghetti Carbonara',
        'description': 'Classic Italian pasta dish with eggs, cheese, and bacon',
        'ingredients': json.dumps([
            '400g spaghetti',
            '200g bacon or pancetta',
            '4 large eggs',
            '100g Parmesan cheese',
            'Black pepper',
            'Salt to taste'
        ]),
        'instructions': '''1. Bring a large pot of salted water to boil and cook spaghetti.
2. Fry bacon until crispy in a large pan.
3. Whisk eggs with grated Parmesan cheese.
4. Drain pasta and mix with bacon.
5. Remove from heat and quickly stir in egg mixture.
6. Season with black pepper and serve immediately.''',
        'image_url': 'https://images.unsplash.com/photo-1612874742237-6526221588e3?w=800',
        'prep_time': 10,
        'cook_time': 20,
        'servings': 4,
        'author': 'Chef Mario'
    },
    {
        'title': 'Chocolate Chip Cookies',
        'description': 'Soft and chewy homemade chocolate chip cookies',
        'ingredients': json.dumps([
            '2 cups all-purpose flour',
            '1 cup butter, softened',
            '1 cup sugar',
            '2 large eggs',
            '2 cups chocolate chips',
            '1 tsp vanilla extract',
            '1 tsp baking soda',
            'Pinch of salt'
        ]),
        'instructions': '''1. Preheat oven to 350°F (175°C).
2. Mix butter and sugar until creamy.
3. Add eggs and vanilla, beat well.
4. Stir in flour, baking soda, and salt.
5. Fold in chocolate chips.
6. Drop spoonfuls onto baking sheet.
7. Bake for 10-12 minutes until golden.
8. Cool and enjoy!''',
        'image_url': 'https://images.unsplash.com/photo-1499636136210-6f4ee915583e?w=800',
        'prep_time': 15,
        'cook_time': 12,
        'servings': 24,
        'author': 'Baker Sue'
    },
    {
        'title': 'Chicken Tikka Masala',
        'description': 'Popular Indian curry dish with tender chicken in creamy tomato sauce',
        'ingredients': json.dumps([
            '600g chicken breast, cubed',
            '1 cup plain yogurt',
            '2 tbsp lemon juice',
            '2 tsp garam masala',
            '1 tsp turmeric',
            '400g crushed tomatoes',
            '1 cup heavy cream',
            '1 onion, diced',
            '3 cloves garlic',
            'Fresh cilantro'
        ]),
        'instructions': '''1. Marinate chicken in yogurt, lemon juice, and spices for 1 hour.
2. Cook chicken in a pan until browned, set aside.
3. Sauté onion, garlic, and ginger in the same pan.
4. Add tomatoes and spices, simmer for 10 minutes.
5. Stir in cream and cooked chicken.
6. Simmer for 10 more minutes.
7. Garnish with cilantro and serve with rice.''',
        'image_url': 'https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=800',
        'prep_time': 75,
        'cook_time': 30,
        'servings': 6,
        'author': 'Chef Priya'
    },
    {
        'title': 'Greek Salad',
        'description': 'Fresh Mediterranean salad with vegetables, olives, and feta',
        'ingredients': json.dumps([
            '3 large tomatoes, cut into wedges',
            '1 cucumber, sliced',
            '1 red onion, thinly sliced',
            '1 green bell pepper',
            '200g feta cheese',
            '1 cup Kalamata olives',
            '1/4 cup olive oil',
            '2 tbsp red wine vinegar',
            'Oregano',
            'Salt and pepper'
        ]),
        'instructions': '''1. Chop all vegetables into bite-sized pieces.
2. Add olives and feta cheese cubes.
3. Whisk together olive oil, vinegar, oregano, salt, and pepper.
4. Pour dressing over salad and toss gently.
5. Let sit for 10 minutes before serving.
6. Enjoy as a side dish or light meal!''',
        'image_url': 'https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?w=800',
        'prep_time': 15,
        'cook_time': 0,
        'servings': 4,
        'author': 'Chef Nikos'
    },
    {
        'title': 'Banana Bread',
        'description': 'Moist and delicious homemade banana bread',
        'ingredients': json.dumps([
            '3 ripe bananas, mashed',
            '1/3 cup melted butter',
            '3/4 cup sugar',
            '1 egg, beaten',
            '1 tsp vanilla extract',
            '1 tsp baking soda',
            'Pinch of salt',
            '1 1/2 cups all-purpose flour',
            '1/2 cup walnuts (optional)'
        ]),
        'instructions': '''1. Preheat oven to 350°F (175°C).
2. Grease a 9x5 inch loaf pan.
3. Mix mashed bananas and melted butter.
4. Stir in sugar, egg, and vanilla.
5. Add baking soda and salt, mix well.
6. Fold in flour until just combined.
7. Add walnuts if desired.
8. Pour into loaf pan and bake for 60-65 minutes.
9. Cool before slicing.''',
        'image_url': 'https://images.unsplash.com/photo-1586444248902-2f64eddc13df?w=800',
        'prep_time': 10,
        'cook_time': 65,
        'servings': 8,
        'author': 'Home Baker Sarah'
    }
]

# Create recipes
print("Adding recipes to database...")
for data in recipes_data:
    recipe, created = Recipe.objects.get_or_create(
        title=data['title'],
        defaults=data
    )
    if created:
        print(f"✅ Created: {recipe.title}")
    else:
        print(f"ℹ️  Already exists: {recipe.title}")

print(f"\n🎉 Done! Total recipes in database: {Recipe.objects.count()}")