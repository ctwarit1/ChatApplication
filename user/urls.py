from django.urls import path
from django.urls import re_path
from . import consumers
from user import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),

]
