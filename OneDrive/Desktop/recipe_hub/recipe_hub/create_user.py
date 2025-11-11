import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_hub.settings')
django.setup()

from django.contrib.auth.models import User

# Create a new user
user = User.objects.create_user(
    username='testuser',
    email='test@example.com',
    password='testpass123'
)
print(f"✅ User created: {user.username}")

# View all users
print("\n📋 All Users:")
users = User.objects.all()
for user in users:
    print(f"  - Username: {user.username}, Email: {user.email}")

# Check if user exists
admin_exists = User.objects.filter(username='admin').exists()
print(f"\n🔍 Admin exists: {admin_exists}")