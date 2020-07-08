from django.urls import path

from . import views

# A list of all the allowable urls for the app

# uniquely identify all the urls to the app
app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name ="entry"),
]
