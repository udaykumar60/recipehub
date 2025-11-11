from django.contrib import admin
from django.shortcuts import redirect
from django.contrib import messages
from .models import Recipe, Category
import json
import os
import subprocess

# Register Category in Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'recipe_count', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    
    def recipe_count(self, obj):
        """Show number of recipes in this category"""
        return obj.recipes.count()
    recipe_count.short_description = 'Recipes'


# Recipe Admin
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'prep_time', 'cook_time', 'servings', 'created_at']
    list_filter = ['created_at', 'category', 'author']
    search_fields = ['title', 'description', 'author__username']
    
    actions = ['export_all_to_excel']
    
    def export_all_to_excel(self, request, queryset):
        """Export database to Excel"""
        try:
            # Get the project directory
            project_dir = os.path.dirname(os.path.abspath(__file__))
            project_dir = os.path.dirname(project_dir)
            
            result = subprocess.run(
                ['python', 'export_to_excel.py'],
                capture_output=True,
                text=True,
                cwd=project_dir
            )
            
            if result.returncode == 0:
                self.message_user(request, "✅ Excel file updated: RecipeHub_Database.xlsx")
            else:
                self.message_user(request, f"❌ Error: {result.stderr}", level='ERROR')
        except Exception as e:
            self.message_user(request, f"❌ Error: {str(e)}", level='ERROR')
    
    export_all_to_excel.short_description = "📊 Export ALL to Excel"
    
    def save_model(self, request, obj, form, change):
        if isinstance(obj.ingredients, list):
            obj.ingredients = json.dumps(obj.ingredients)
        super().save_model(request, obj, form, change)
    
    def has_delete_permission(self, request, obj=None):
        return request.user.is_staff