from .forms import RecipeForm
from django.contrib import messages
from django.shortcuts import render, redirect


# Create your views here.
def add(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ("Added recipe."))
            return redirect("/")
        else:
            messages.error(request, ("Failed to add recipe, try again."))
    form = RecipeForm()
    return render(request, "recipe/add.html", {'form': form})


def index(request):
    return render(request, "index.html")
