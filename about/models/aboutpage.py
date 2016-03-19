from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from blog.blogstreamblock import BlogStreamBlock
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel

class AboutPage(Page):
    body = StreamField(BlogStreamBlock(), blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]