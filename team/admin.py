from django.contrib import admin
from django.utils.html import format_html

from .models import Team
# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html(f'<img src="{object.photo.url}" width="40" style="border-radius: 40px;"/>')
    thumbnail.short_description = "Photo"

    model = Team
    list_display = ['id','thumbnail','first_name','last_name','designation','created']
    list_display_links = ['id','first_name']
    ordering = ['created']
    search_fields = ['first_name','last_name','designation']
    list_filter = ['designation']