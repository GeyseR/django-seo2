from django import template

register = template.Library()


@register.inclusion_tag('djangoseo/templatetags/seo_text.html')
def seo_text(seo_data):
    return {'seo_data': seo_data}
