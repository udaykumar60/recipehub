import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_hub.settings')
django.setup()

from recipes.models import Recipe
from django.contrib.auth.models import User
import json

# Create a default admin user if doesn't exist
admin_user, created = User.objects.get_or_create(
    username='admin',
    defaults={'email': 'admin@recipehub.com', 'is_staff': True, 'is_superuser': True}
)
if created:
    admin_user.set_password('admin123')
    admin_user.save()
    print("✅ Admin user created (username: admin, password: admin123)")

recipes_data = [
    # Indian
    {
        'title': 'Butter Chicken',
        'description': 'Creamy and flavorful Indian curry with tender chicken',
        'ingredients': json.dumps([
            '500g chicken breast',
            '2 cups tomato puree',
            '1 cup heavy cream',
            '3 tbsp butter',
            '2 tsp garam masala',
            '1 tsp turmeric',
            '4 cloves garlic',
            '1 inch ginger',
            'Salt to taste'
        ]),
        'instructions': '1. Marinate chicken with yogurt and spices for 2 hours\n2. Cook chicken in butter until golden\n3. Add tomato puree and spices\n4. Simmer for 20 minutes\n5. Add cream and cook for 5 more minutes\n6. Serve with rice or naan',
        'image_url': 'https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=800',
        'prep_time': 30,
        'cook_time': 40,
        'servings': 4,
        'category': 'indian',
        'author': admin_user
    },
    {
        'title': 'Biryani',
        'description': 'Aromatic rice dish with spiced meat and vegetables',
        'ingredients': json.dumps([
            '2 cups basmati rice',
            '500g chicken or mutton',
            '2 onions sliced',
            '1 cup yogurt',
            '2 tsp biryani masala',
            '1 tsp saffron',
            'Fresh mint and cilantro',
            '4 cups water'
        ]),
        'instructions': '1. Soak rice for 30 minutes\n2. Marinate meat with yogurt and spices\n3. Fry onions until golden\n4. Layer rice and meat in pot\n5. Add saffron milk on top\n6. Cook on low heat for 45 minutes\n7. Serve hot with raita',
        'image_url': 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=800',
        'prep_time': 45,
        'cook_time': 60,
        'servings': 6,
        'category': 'indian',
        'author': admin_user
    },
    
    # Chinese
    {
        'title': 'Kung Pao Chicken',
        'description': 'Spicy stir-fried chicken with peanuts and vegetables',
        'ingredients': json.dumps([
            '500g chicken breast cubed',
            '1 cup roasted peanuts',
            '3 bell peppers',
            '4 dried red chilies',
            '3 tbsp soy sauce',
            '2 tbsp rice vinegar',
            '1 tbsp sugar',
            '2 cloves garlic',
            '1 tsp cornstarch'
        ]),
        'instructions': '1. Marinate chicken with soy sauce and cornstarch\n2. Heat oil in wok\n3. Stir-fry chicken until cooked\n4. Add vegetables and chilies\n5. Add sauce mixture\n6. Toss in peanuts\n7. Serve over rice',
        'image_url': 'https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=800',
        'prep_time': 20,
        'cook_time': 15,
        'servings': 4,
        'category': 'chinese',
        'author': admin_user
    },
    {
        'title': 'Fried Rice',
        'description': 'Classic Chinese fried rice with vegetables and eggs',
        'ingredients': json.dumps([
            '3 cups cooked rice (day old)',
            '2 eggs',
            '1 cup mixed vegetables',
            '3 tbsp soy sauce',
            '2 green onions',
            '2 cloves garlic',
            '1 tbsp sesame oil',
            'Salt and pepper'
        ]),
        'instructions': '1. Heat wok with oil\n2. Scramble eggs and set aside\n3. Stir-fry vegetables\n4. Add rice and break up clumps\n5. Add soy sauce and sesame oil\n6. Toss in eggs\n7. Garnish with green onions',
        'image_url': 'https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=800',
        'prep_time': 15,
        'cook_time': 10,
        'servings': 4,
        'category': 'chinese',
        'author': admin_user
    },
    
    # Italian
    {
        'title': 'Spaghetti Carbonara',
        'description': 'Classic Italian pasta with creamy egg sauce and bacon',
        'ingredients': json.dumps([
            '400g spaghetti',
            '200g bacon or pancetta',
            '4 egg yolks',
            '100g Parmesan cheese',
            '2 cloves garlic',
            'Black pepper',
            'Salt',
            'Pasta water'
        ]),
        'instructions': '1. Cook pasta in salted water\n2. Fry bacon until crispy\n3. Mix egg yolks with Parmesan\n4. Drain pasta, reserve 1 cup water\n5. Toss pasta with bacon\n6. Remove from heat, add egg mixture\n7. Add pasta water to create creamy sauce\n8. Season with black pepper',
        'image_url': 'https://images.unsplash.com/photo-1612874742237-6526221588e3?w=800',
        'prep_time': 10,
        'cook_time': 20,
        'servings': 4,
        'category': 'italian',
        'author': admin_user
    },
    {
        'title': 'Margherita Pizza',
        'description': 'Simple and delicious pizza with tomato, mozzarella, and basil',
        'ingredients': json.dumps([
            '1 pizza dough',
            '1 cup tomato sauce',
            '200g fresh mozzarella',
            'Fresh basil leaves',
            '2 tbsp olive oil',
            'Salt',
            'Oregano'
        ]),
        'instructions': '1. Preheat oven to 475°F (245°C)\n2. Roll out pizza dough\n3. Spread tomato sauce\n4. Add sliced mozzarella\n5. Drizzle with olive oil\n6. Bake for 12-15 minutes\n7. Top with fresh basil\n8. Serve hot',
        'image_url': 'https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=800',
        'prep_time': 20,
        'cook_time': 15,
        'servings': 2,
        'category': 'italian',
        'author': admin_user
    },
    
    # Mexican
    {
        'title': 'Tacos Al Pastor',
        'description': 'Mexican street tacos with marinated pork and pineapple',
        'ingredients': json.dumps([
            '500g pork shoulder',
            '3 dried chilies',
            '1 cup pineapple chunks',
            '1 onion',
            'Corn tortillas',
            '3 cloves garlic',
            'Cilantro',
            'Lime wedges'
        ]),
        'instructions': '1. Blend chilies, garlic, and spices for marinade\n2. Marinate pork for 4 hours\n3. Grill or pan-fry pork\n4. Chop into small pieces\n5. Warm tortillas\n6. Fill with pork and pineapple\n7. Top with onion and cilantro\n8. Serve with lime',
        'image_url': 'https://images.unsplash.com/photo-1565299585323-38d6b0865b47?w=800',
        'prep_time': 240,
        'cook_time': 20,
        'servings': 6,
        'category': 'mexican',
        'author': admin_user
    },
    
    # American
    {
        'title': 'Classic Burger',
        'description': 'Juicy beef burger with all the fixings',
        'ingredients': json.dumps([
            '500g ground beef',
            '4 burger buns',
            '4 slices cheese',
            'Lettuce',
            'Tomato slices',
            'Onion slices',
            'Pickles',
            'Ketchup and mustard',
            'Salt and pepper'
        ]),
        'instructions': '1. Form beef into 4 patties\n2. Season with salt and pepper\n3. Grill or pan-fry for 4 minutes each side\n4. Add cheese in last minute\n5. Toast buns\n6. Assemble burger with toppings\n7. Serve with fries',
        'image_url': 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=800',
        'prep_time': 15,
        'cook_time': 10,
        'servings': 4,
        'category': 'american',
        'author': admin_user
    },
    
    # Japanese
    {
        'title': 'Chicken Teriyaki',
        'description': 'Sweet and savory glazed chicken',
        'ingredients': json.dumps([
            '500g chicken thighs',
            '1/2 cup soy sauce',
            '1/4 cup mirin',
            '2 tbsp sugar',
            '2 cloves garlic',
            '1 inch ginger',
            'Sesame seeds',
            'Green onions'
        ]),
        'instructions': '1. Mix soy sauce, mirin, and sugar for sauce\n2. Cook chicken in pan until golden\n3. Pour sauce over chicken\n4. Simmer until sauce thickens\n5. Garnish with sesame seeds\n6. Serve over rice with vegetables',
        'image_url': 'https://images.unsplash.com/photo-1582169296194-e4d644c48063?w=800',
        'prep_time': 10,
        'cook_time': 25,
        'servings': 4,
        'category': 'japanese',
        'author': admin_user
    },
    
    # Desserts
    {
        'title': 'Chocolate Chip Cookies',
        'description': 'Soft and chewy classic cookies',
        'ingredients': json.dumps([
            '2 cups flour',
            '1 cup butter softened',
            '1 cup brown sugar',
            '1/2 cup white sugar',
            '2 eggs',
            '2 tsp vanilla extract',
            '2 cups chocolate chips',
            '1 tsp baking soda',
            '1/2 tsp salt'
        ]),
        'instructions': '1. Preheat oven to 375°F (190°C)\n2. Cream butter and sugars\n3. Beat in eggs and vanilla\n4. Mix in flour, baking soda, and salt\n5. Fold in chocolate chips\n6. Drop spoonfuls on baking sheet\n7. Bake for 10-12 minutes\n8. Cool on wire rack',
        'image_url': 'https://images.unsplash.com/photo-1499636136210-6f4ee915583e?w=800',
        'prep_time': 15,
        'cook_time': 12,
        'servings': 24,
        'category': 'desserts',
        'author': admin_user
    },
    {
        'title': 'Tiramisu',
        'description': 'Italian coffee-flavored dessert',
        'ingredients': json.dumps([
            '6 egg yolks',
            '3/4 cup sugar',
            '1 1/3 cups mascarpone cheese',
            '2 cups heavy cream',
            '2 cups strong coffee',
            '3 tbsp rum or coffee liqueur',
            'Ladyfinger cookies',
            'Cocoa powder'
        ]),
        'instructions': '1. Whisk egg yolks and sugar until thick\n2. Add mascarpone and mix\n3. Whip cream and fold in\n4. Mix coffee and rum\n5. Dip ladyfingers in coffee\n6. Layer cookies and cream mixture\n7. Refrigerate 4 hours\n8. Dust with cocoa before serving',
        'image_url': 'https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=800',
        'prep_time': 30,
        'cook_time': 0,
        'servings': 8,
        'category': 'desserts',
        'author': admin_user
    },
    
    # Beverages
    {
        'title': 'Mango Lassi',
        'description': 'Refreshing Indian yogurt drink',
        'ingredients': json.dumps([
            '2 ripe mangoes',
            '1 cup yogurt',
            '1/2 cup milk',
            '3 tbsp sugar',
            '1/4 tsp cardamom powder',
            'Ice cubes',
            'Saffron strands (optional)'
        ]),
        'instructions': '1. Peel and chop mangoes\n2. Blend mango, yogurt, milk, and sugar\n3. Add cardamom powder\n4. Blend until smooth\n5. Add ice and blend again\n6. Pour into glasses\n7. Garnish with saffron\n8. Serve chilled',
        'image_url': 'https://images.unsplash.com/photo-1577805947697-89e18249d767?w=800',
        'prep_time': 10,
        'cook_time': 0,
        'servings': 4,
        'category': 'beverages',
        'author': admin_user
    },
]

# Clear existing recipes (optional)
Recipe.objects.all().delete()

# Add new recipes
for data in recipes_data:
    Recipe.objects.create(**data)
    print(f"✅ Added: {data['title']}")

print(f"\n🎉 Successfully added {len(recipes_data)} recipes!")
print("\n👤 Login credentials:")
print("   Username: admin")
print("   Password: admin123")
