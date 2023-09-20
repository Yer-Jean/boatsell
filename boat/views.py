from django.shortcuts import render
from django.views.generic import ListView

from boat.models import Boat


class BoatListView(ListView):
    model = Boat

