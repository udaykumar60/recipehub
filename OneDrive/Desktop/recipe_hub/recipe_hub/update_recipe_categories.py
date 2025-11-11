import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_hub.settings')
django.setup()

from recipes.models import Recipe, Category

# Map old category codes to new Category objects
category_mapping = {
    'indian': 'Indian',
    'chinese': 'Chinese',
    'italian': 'Italian',
    'mexican': 'Mexican',
    'american': 'American',
    'japanese': 'Japanese',
    'desserts': 'Desserts',
    'beverages': 'Beverages',
    'other': None,
}

for recipe in Recipe.objects.all():
    # If recipe has old category field value
    if hasattr(recipe, '_category_old'):
        old_category = recipe._category_old
        new_category_name = category_mapping.get(old_category)
        
        if new_category_name:
            try:
                category = Category.objects.get(name=new_category_name)
                recipe.category = category
                recipe.save()
                print(f"✅ Updated: {recipe.title} → {category.name}")
            except Category.DoesNotExist:
                print(f"⚠️ Category not found: {new_category_name}")

print("\n🎉 All recipes updated!")