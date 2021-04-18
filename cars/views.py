from django.shortcuts import render
from django.views.generic import (
ListView,DetailView,
)

from .models import Car
# Create your views here.

class CarsListView(ListView):
    model = Car
    paginate_by = 3

class CarsDetailView(DetailView):
    model = Car
