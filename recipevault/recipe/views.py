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
    return render(request, "index.html")


def view(request, rid):
    return render(request, "{rid}")


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
