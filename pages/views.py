from django.shortcuts import render

from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/home.html '


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class ServicesPageView(TemplateView):
    template_name = 'pages/services.html'


class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'
