from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.db.models import Q
from .models import Recipe, Category  # ADD Category here
import json
import os

def recipe_list(request):
    recipes = Recipe.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        recipes = recipes.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(ingredients__icontains=search_query)
        )
    
    # Category filter
    category_slug = request.GET.get('category', '')
    if category_slug:
        recipes = recipes.filter(category__slug=category_slug)
    
    # Get all categories
    categories = Category.objects.all()
    
    return render(request, 'recipes/recipe_list.html', {
        'recipes': recipes,
        'total_recipes': recipes.count(),
        'categories': categories,
        'search_query': search_query,
        'selected_category': category_slug,
    })

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    
    # Get ingredients as list
    try:
        ingredients = json.loads(recipe.ingredients)
    except:
        ingredients = recipe.ingredients.split('\n')
    
    # Check if user can delete (only admin or recipe owner)
    can_delete = request.user.is_staff or (request.user.is_authenticated and recipe.author == request.user)
    
    return render(request, 'recipes/recipe_detail.html', {
        'recipe': recipe,
        'ingredients': ingredients,
        'can_delete': can_delete,
    })

@login_required
def recipe_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')
        image_url = request.POST.get('image_url')
        prep_time = request.POST.get('prep_time', 0)
        cook_time = request.POST.get('cook_time', 0)
        servings = request.POST.get('servings', 1)
        category_id = request.POST.get('category')
        
        # Convert ingredients to JSON list
        ingredients_list = [ing.strip() for ing in ingredients.split('\n') if ing.strip()]
        ingredients_json = json.dumps(ingredients_list)
        
        # Get category object
        category = None
        if category_id:
            try:
                category = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                pass
        
        Recipe.objects.create(
            title=title,
            description=description,
            ingredients=ingredients_json,
            instructions=instructions,
            image_url=image_url,
            prep_time=prep_time,
            cook_time=cook_time,
            servings=servings,
            category=category,
            author=request.user
        )
        
        messages.success(request, 'Recipe created successfully!')
        return redirect('recipe_list')
    
    categories = Category.objects.all()
    return render(request, 'recipes/recipe_create.html', {'categories': categories})

@login_required
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    
    # Only admin or recipe owner can delete
    if request.user.is_staff or recipe.author == request.user:
        recipe.delete()
        messages.success(request, 'Recipe deleted successfully!')
    else:
        messages.error(request, 'You do not have permission to delete this recipe.')
    
    return redirect('recipe_list')

def user_signup(request):
    if request.user.is_authenticated:
        return redirect('recipe_list')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        # Validation
        if password != password_confirm:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'recipes/signup.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'recipes/signup.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'recipes/signup.html')
        
        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        messages.success(request, f'Welcome to RecipeHub, {username}!')
        return redirect('recipe_list')
    
    return render(request, 'recipes/signup.html')

def user_login(request):
    if request.user.is_authenticated:
        return redirect('recipe_list')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('recipe_list')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'recipes/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('recipe_list')

@staff_member_required
def export_to_excel_view(request):
    """Export database to Excel - Admin only"""
    try:
        import subprocess
        result = subprocess.run(
            ['python', 'export_to_excel.py'],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )
        
        if result.returncode == 0:
            messages.success(request, '✅ Excel file updated successfully! Check: RecipeHub_Database.xlsx')
        else:
            messages.error(request, f'❌ Export failed: {result.stderr}')
    except Exception as e:
        messages.error(request, f'❌ Error: {str(e)}')
    
    return redirect('recipe_list')