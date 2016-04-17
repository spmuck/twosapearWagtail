from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from blog.video import Video


class VideoPage(Page):
    def get_context(self, request):
        context = super(VideoPage, self).get_context(request)
        context['videos'] = Video.objects.all().filter(show_video="true").order_by('date')
        return context
