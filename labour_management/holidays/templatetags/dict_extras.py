from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """
    Given a dict and a key, return dictionary[key] or None.
    Usage in template: {{ matrix|get_item:employee.id|get_item:date }}
    """
    if dictionary is None:
        return None
    return dictionary.get(key)
