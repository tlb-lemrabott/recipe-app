from django.http import JsonResponse
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator

@api_view(['GET', 'POST'])
def recipe_list(request, format=None):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        limit = request.GET.get('limit', 10)
        
        try:
            page = int(page)
            limit = int(limit)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        recipes = Recipe.objects.all()
        paginator = Paginator(recipes, limit)
        
        try:
            recipes_page = paginator.page(page)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = RecipeSerializer(recipes_page, many=True)
        return JsonResponse({
            'recipes': serializer.data,
            'count': paginator.count,
            'num_pages': paginator.num_pages,
            'current_page': page
        }, safe=False)
    
    elif request.method == 'POST':
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def recipe_detail(request, id, format=None):
    try:
        recipe = Recipe.objects.get(pk=id)
    except Recipe.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RecipeSerializer(recipe, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)