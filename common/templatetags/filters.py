from django import template
from django.conf import settings
import locale

locale.setlocale(locale.LC_ALL, settings.LANGUAGE_CODE)
register = template.Library()


@register.filter(name='currency')
def currency(value):
    return locale.currency(value, grouping=True)

@register.filter(is_safe=False)
def add(value, arg):
    """Multiply the arg to the value."""
    try:
        return int(value) + int(arg)
    except (ValueError, TypeError):
        try:
            return value + arg
        except Exception:
            return ''
