from django.db import models

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, InlinePanel, StreamFieldPanel)
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase

from blog.carousel import CarouselItem
from blog.blogstreamblock import BlogStreamBlock

class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('blog.BlogPage', related_name='tagged_items')
    
class BlogPageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey('blog.BlogPage', related_name='carousel_items')

class BlogPage(Page):
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = StreamField(BlogStreamBlock())
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    feed_title = models.CharField(max_length=250, blank=True, null=True)
    feed_description = models.CharField(max_length=250, blank=True, null=True)
    is_recipe = models.BooleanField()

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
        index.SearchField('body'),
    )

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        ImageChooserPanel('main_image'),
        FieldPanel('intro'),
        StreamFieldPanel('body'),
        InlinePanel('carousel_items', label="Carousel items"),
        FieldPanel('is_recipe'),
    ]
    
    promote_panels = Page.promote_panels + [
        ImageChooserPanel('feed_image'),
        FieldPanel('tags'),
        FieldPanel('feed_title'),
        FieldPanel('feed_description'),
    ]