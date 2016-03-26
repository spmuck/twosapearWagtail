from django import template
from blog.models import BlogPage
from django.conf import settings

register = template.Library()

@register.inclusion_tag('blog/tags/social_meta.html', takes_context=True)
def social_meta(context, calling_page=None):
    if calling_page.feed_image:
        feed_image = calling_page.feed_image
    elif calling_page.main_image:
        feed_image = calling_page.main_image
    if calling_page.feed_title:
        feed_title = calling_page.feed_title
    elif calling_page.title:
        feed_title = calling_page.title
    if calling_page.feed_description:
        feed_description = calling_page.feed_description
    elif calling_page.intro:
        feed_description = calling_page.intro
    return {
        'calling_page': calling_page,
        'feed_image' : feed_image,
        'feed_title' : feed_title,
        'feed_description' : feed_description,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }

@register.inclusion_tag('blog/tags/social_drop_down.html', takes_context=True)
def social_drop_down(context, calling_page=None):
    if calling_page.feed_image:
        feed_image = calling_page.feed_image
    elif calling_page.main_image:
        feed_image = calling_page.main_image
    if calling_page.feed_title:
        feed_title = calling_page.feed_title
    elif calling_page.title:
        feed_title = calling_page.title
    if calling_page.feed_description:
        feed_description = calling_page.feed_description
    elif calling_page.intro:
        feed_description = calling_page.intro
    return {
        'page': calling_page,
        'feed_image' : feed_image,
        'feed_title' : feed_title,
        'feed_description' : feed_description,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }

@register.assignment_tag()    
def get_domain():
    return settings.DOMAIN