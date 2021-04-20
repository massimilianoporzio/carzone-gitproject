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
        if 'model' in self.request.GET:
            model = self.request.GET['model']
            cars = cars.filter(
                Q(model__iexact=model)
            )

        if 'city' in self.request.GET:
            city = self.request.GET['city']
            cars = cars.filter(
                Q(city__iexact=city)
            )
        if 'year' in self.request.GET:
            year = self.request.GET['year']
            cars = cars.filter(
                Q(year__exact=year)
            )
        if 'body-style' in self.request.GET:
            style = self.request.GET['body-style']
            cars = cars.filter(
                Q(body_style__iexact=style)
            )
        if 'min_price' in self.request.GET:
            min_price = self.request.GET['min_price']
            max_price = self.request.GET['max_price']
            if max_price:
                cars = cars.filter(price__gte=min_price, price__lte=max_price)
            else:
                cars = cars.filter(price__gte=min_price)
        else:
            print('BAZINGA!')

        context['cars'] = cars
        return context

    template_name = 'cars/search.html'
