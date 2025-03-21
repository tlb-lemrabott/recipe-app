from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'image_url', 'title', 'rate', 'description', 'ingredients', 'instructions', 'created_at', 'updated_at']