from django.shortcuts import render
from django.http import HttpRequest


# Create your views here.
def index(request: HttpRequest):
    return render(request, "index.html")


def room(request, room_name):
    return render(request, "room.html", {"room_name": room_name})
