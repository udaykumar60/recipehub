from django.db import models
from django.contrib.auth.models import User
import json

class Category(models.Model):
    """Recipe Category Model - Admins can add new categories"""
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Auto-generate slug if not provided
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()  # Store as JSON string
    instructions = models.TextField()
    image_url = models.URLField(max_length=500, blank=True, null=True)
    prep_time = models.IntegerField(default=0)
    cook_time = models.IntegerField(default=0)
    servings = models.IntegerField(default=1)
    
    # NEW: ForeignKey to Category instead of hardcoded choices
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='recipes'
    )
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_ingredients_list(self):
        """Convert JSON string to list"""
        try:
            return json.loads(self.ingredients)
        except:
            return self.ingredients.split('\n')
    
    def set_ingredients_list(self, ingredients_list):
        """Convert list to JSON string"""
        self.ingredients = json.dumps(ingredients_list)
    
    def get_total_time(self):
        return self.prep_time + self.cook_time