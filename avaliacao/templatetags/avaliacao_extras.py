from django import template

register = template.Library()

@register.simple_tag
def questionario_form(*args, **kwargs):
    return render_form(*args, **kwargs)
