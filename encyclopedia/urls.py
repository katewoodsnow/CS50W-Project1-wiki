from django.urls import path

from . import views

# A list of all the allowable urls for the app
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki, name = "wiki"),
]
