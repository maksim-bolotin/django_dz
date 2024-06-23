from django import template

register = template.Library()


@register.filter(name='safe_image_url')
def safe_image_url(image_field):
    if image_field and hasattr(image_field, 'url'):
        return image_field.url
    return ''
