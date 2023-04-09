from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("view/<int:rid>", views.view, name="view"),
    path("edit/<int:rid>", views.edit, name="edit"),
]