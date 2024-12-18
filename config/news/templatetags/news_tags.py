from django import template


from ..models import Type, Flower




register = template.Library()

@register.simple_tag
def all_types():
    return Type.objects.all()

