from django.test import TestCase, RequestFactory
from django.urls import reverse
from recipe.models import Recipe
from recipe.views import main, recipe_detail


class MainViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_main_view(self):
        recipe = Recipe.objects.create(
            name='Test Recipe',
            created_at='2023-01-01'
        )

        url = reverse('main')
        request = self.factory.get(url)
        response = main(request)

        self.assertEqual(response.status_code, 200)

        self.assertIn(recipe, response.context['recipes'])

    def test_main_view_no_recipes(self):
        url = reverse('main')
        request = self.factory.get(url)
        response = main(request)

        self.assertEqual(response.status_code, 200)

        self.assertQuerysetEqual(response.context['recipes'], [])


class RecipeDetailViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.recipe = Recipe.objects.create(
            name='Test Recipe',
            created_at='2023-01-01'
        )

    def test_recipe_detail_view(self):
        url = reverse('recipe_detail', args=[self.recipe.id])
        request = self.factory.get(url)
        response = recipe_detail(request, recipe_id=self.recipe.id)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.context['recipe'], self.recipe)

    def test_recipe_detail_view_invalid_id(self):
        invalid_id = self.recipe.id + 1
        url = reverse('recipe_detail', args=[invalid_id])
        request = self.factory.get(url)
        response = recipe_detail(request, recipe_id=invalid_id)

        self.assertEqual
