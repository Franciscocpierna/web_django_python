import os

from django.db.models import Q
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.http.response import Http404
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from utils.pagination import make_pagination

from recipes.models import Recipe

PER_PAGE = int(os.environ.get('PER_PAGE', 6))


# def theory(request, *args, **kwargs):
#     return render(
#         request,
#         'recipes/pages/theory.html'
#     )

def theory(request, *args, **kwargs):
    recipes = Recipe.objects.all()
    recipes = recipes.filter(title__icontains='Teste')

    context = {
        'recipes': recipes
    }

    return render(
        request,
        'recipes/pages/theory.html',
        context=context
    )
