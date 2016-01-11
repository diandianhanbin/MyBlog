from django import template
from django.utils.safestring import mark_safe
import markdown as mkdn

register = template.Library()


@register.filter
def markdown(value, smode=None):
    return mark_safe(mkdn.markdown(value, safe_mode='escape'))
