from django.urls import path

from .views import (
    HomePageView,AboutPageView,
    ServicesPageView,ContactPageView
)

app_name='pages'

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('about',AboutPageView.as_view(),name='about'),
    path('services',ServicesPageView.as_view(),name='services'),
    path('contact',ContactPageView.as_view(),name='contact'),

]