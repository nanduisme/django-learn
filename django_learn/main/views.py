from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

from django.core.handlers.wsgi import WSGIRequest as Response

# Create your views here.

def index(response: Response, id :str):
    ls: ToDoList = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls":ls})

def home(response: Response):
    return render(response, "main/home.html", {})

def create(response: Response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

            return HttpResponseRedirect(f"/{t.id}")

    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})