from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import InlinePanel, FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

class SocialLink(models.Model):
    link_external = models.URLField("External link")
    default_image = models.ForeignKey('wagtailimages.Image', related_name='+')
    hover_image = models.ForeignKey('wagtailimages.Image', related_name='+')
    
    panels = [
        ImageChooserPanel('default_image'),
        ImageChooserPanel('hover_image'),
        FieldPanel('link_external'),
    ]

class SocialLinkItem(Orderable, SocialLink):
    content_object = ParentalKey('blog.SocialMediaLinks', related_name='social_links')

class SocialMediaLinks(Page):
    content_panels = Page.content_panels + [
        InlinePanel('social_links', label="Social LInks")
    ]
    