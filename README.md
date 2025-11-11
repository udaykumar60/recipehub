
[add_categories.py](https://github.com/user-attachments/files/23479862/add_categories.py)
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_hub.settings')
django.setup()

from recipes.models import Category

# Create categories
categories = [
    {'name': 'Indian', 'description': 'Traditional Indian cuisine'},
    {'name': 'Chinese', 'description': 'Authentic Chinese dishes'},
    {'name': 'Italian', 'description': 'Classic Italian recipes'},
    {'name': 'Mexican', 'description': 'Spicy Mexican food'},
    {'name': 'American', 'description': 'American comfort food'},
    {'name': 'Japanese', 'description': 'Japanese cuisine'},
    {'name': 'Desserts', 'description': 'Sweet treats and desserts'},
    {'name': 'Beverages', 'description': 'Drinks and beverages'},
    {'name': 'Breakfast', 'description': 'Morning meals'},
    {'name': 'Vegan', 'description': 'Plant-based recipes'},
    {'name': 'Gluten-Free', 'description': 'No gluten recipes'},
]

for cat_data in categories:
    category, created = Category.objects.get_or_create(
        name=cat_data['name'],
        defaults={'description': cat_data['description']}
    )
    if created:
        print(f"✅ Created: {category.name}")
    else:
        print(f"ℹ️ Already exists: {category.name}")

print(f"\n🎉 Total categories: {Category.objects.count()}")
