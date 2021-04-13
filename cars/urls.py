from django.urls import path

from .views import CarsListView

app_name = 'cars'

urlpatterns = [
        path('',CarsListView.as_view(),name='list'),
]