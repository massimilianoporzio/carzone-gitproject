from django.shortcuts import render

from django.views.generic import TemplateView
from team.models import Team

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/home.html '

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['team'] = Team.objects.all()
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
