from __future__ import unicode_literals

from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from blog.models import BlogPage
from taggit.models import Tag



class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]
    
    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        posts = BlogPage.objects.live().order_by('-date')
        page = request.GET.get('page', 1)
        
        paginator = Paginator(posts, 5)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        
        context['posts'] = posts;
        
        return context
