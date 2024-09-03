from django import template

register = template.Library()

@register.filter
def get_images(property_dict, property_id):
    return property_dict.get(property_id, [])