from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.html import format_html
from .forms import RecipeForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404

from .models import Recipe


# Create your views here.
def add(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            temp = form.save()
            ht = "/view/" + str(temp.id)
            temp2 = format_html('Added recipe. <a href="{}">View Here</a>', ht)
            messages.success(request, temp2)
        else:
            messages.error(request, ("Failed to add recipe, try again."))
    form = RecipeForm()
    return render(request, "recipe/add.html", {'form': form})


def index(request):
    recipes = Recipe.objects.all().order_by('id')
    pages = Paginator(recipes, 9)
    page = request.GET.get('page', 1)
    try:
        recipes2 = pages.page(page)
    except PageNotAnInteger:
        recipes2 = pages.page(1)
    except EmptyPage:
        recipes2 = pages.page(pages.num_pages)
    return render(request, "recipe/index.html", {'recipes': recipes})


def view(request, rid):
    obj = get_object_or_404(Recipe, id=rid)
    return render(request, "recipe/view.html", {'obj': obj})


def edit(request, rid):
    obj = get_object_or_404(Recipe, id=rid)
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            temp = form.save()
            ht = "/view/" + str(temp.id)
            temp2 = format_html('Edited recipe. <a href="{}">View Here</a>', ht)
            messages.success(request, temp2)
        else:
            messages.error(request, ("Failed to edit recipe, try again."))
    form = RecipeForm(instance=obj)
    return render(request, "recipe/edit.html", {'form': form, 'obj': obj})
