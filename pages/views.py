from django.shortcuts import render

from django.views.generic import TemplateView
from team.models import Team
from cars.models import Car
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/home.html '

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['team'] = Team.objects.all()
        context['featured_cars'] = Car.objects.order_by('-created_date').filter(is_featured=True)
        context['last_cars'] = Car.objects.order_by('-created_date')[:2]
        context['all_cars'] = Car.objects.order_by('-created_date')

        search_models = Car.objects.values_list('model',flat=True).distinct().order_by('model')
        search_cities = Car.objects.values_list('city', flat=True).distinct().order_by('city')
        search_years = Car.objects.values_list('year',flat=True).distinct().order_by('year')
        search_styles = Car.objects.values_list('body_style',flat=True).distinct().order_by('body_style')
        context['search_models'] = search_models
        context['search_cities'] = search_cities
        context['search_years'] = search_years
        context['search_styles'] = search_styles
        context['maximum_price'] = 150000
        return context


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['team'] = Team.objects.all()
        return context


class ServicesPageView(TemplateView):
    template_name = 'pages/services.html'


class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'
