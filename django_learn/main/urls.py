from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="Home"),
    path("create/", views.create, name="Create To Do List"),
]