from django import template
from blog.models import BlogPage

register = template.Library()

@register.inclusion_tag('blog/tags/social_meta.html', takes_context=True)
def social_meta(context, calling_page=None):
    if calling_page.feed_image:
        feed_image = calling_page.feed_imgage
    elif calling_page.main_image:
        feed_image = calling_page.main_image
    return {
        'calling_page': calling_page,
        'feed_image' : feed_image,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }