from django.urls import path

from .views import CarsListView,CarsDetailView

app_name = 'cars'

urlpatterns = [
        path('',CarsListView.as_view(),name='list'),
        path('<slug>',CarsDetailView.as_view(), name='detail'),
]