from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("add", views.add_entry, name="add_entry"),
    path("edit", views.edit_entry, name="edit_entry")
]
