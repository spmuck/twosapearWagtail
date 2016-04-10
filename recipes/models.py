from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from blog.models import BlogPage


class RecipePage(Page):
    def get_context(self, request):
        context = super(RecipePage, self).get_context(request)
        context['posts'] = BlogPage.objects.live().filter(is_recipe="true").order_by('date')[:20]
        return context
