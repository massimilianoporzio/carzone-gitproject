from django.contrib import admin

from .models import Car
# Register your models here.

@admin.register(Car)
class CarsAdmin(admin.ModelAdmin):
    model = Car