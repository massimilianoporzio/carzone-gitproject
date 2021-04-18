from django.shortcuts import render

from django.db.models import Q
from django.views.generic import (
    ListView, DetailView, TemplateView
)

from .models import Car


# Create your views here.

class CarsListView(ListView):
    model = Car
    paginate_by = 3


class CarsDetailView(DetailView):
    model = Car


class CarsSearchView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cars = Car.objects.order_by('-created_date')
        if 'q' in self.request.GET:
            q = self.request.GET['q']
            cars = cars.filter(
                Q(description__icontains=q)
            )
        context['cars'] = cars
        return context

    template_name = 'cars/search.html'
