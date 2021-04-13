from django.shortcuts import render
from django.views.generic import ListView

from .models import Car
# Create your views here.

class CarsListView(ListView):
    model = Car
