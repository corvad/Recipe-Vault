from django.urls import reverse
from django.utils.html import format_html
from .forms import RecipeForm
from django.contrib import messages
from django.shortcuts import render, redirect


# Create your views here.
def add(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            temp = form.save()
            ht = "/view/" + str(temp.id)
            temp2 = format_html('Added recipe. <a href="{}">View Here</a>', reverse(ht))
            messages.success(request, temp2)
        else:
            messages.error(request, ("Failed to add recipe, try again."))
    form = RecipeForm()
    return render(request, "recipe/add.html", {'form': form})


def index(request):
    return render(request, "index.html")
