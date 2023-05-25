from django.shortcuts import render, get_object_or_404
from recipe.models import Recipe


def main(request):
    recipes = Recipe.objects.filter(created_at__year=2023)
    context = {'recipes': recipes}
    return render(request, 'main.html', context)


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    context = {'recipe': recipe}
    return render(request, 'recipe_detail.html', context)
