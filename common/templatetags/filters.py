from django import template
from django.conf import settings
import locale

locale.setlocale(locale.LC_ALL, settings.LANGUAGE_CODE)
register = template.Library()


@register.filter(name='currency')
def currency(value):
    return locale.currency(value, grouping=True)
