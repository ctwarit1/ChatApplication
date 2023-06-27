from django.shortcuts import render
from .models import Message, Group
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    group = Group.objects.filter(name=room_name).first()
    if group:
        pass
    else:
        group = Group(name=room_name)
        group.save()

    return render(request, "chat/room.html", {"room_name": room_name})
