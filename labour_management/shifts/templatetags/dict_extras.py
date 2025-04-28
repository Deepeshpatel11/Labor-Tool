from django import template

register = template.Library()

@register.filter
def get_item(dict_obj, key):
    return dict_obj.get(key)

@register.filter
def replace(value, old, new):
    try:
        return value.replace(old, new)
    except Exception:
        return value
