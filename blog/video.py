from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
import datetime

@register_snippet
class Video(models.Model):
    title = models.CharField(max_length=40)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    embed_url = models.URLField("Embed URL", blank=True)
    caption = models.CharField(max_length=255, blank=True)
    show_video = models.BooleanField(default=True)
    date = models.DateField(default=datetime.date.today())
    
    def __str__(self):
        return self.title

    panels = [
        FieldPanel('title'),
        ImageChooserPanel('image'),
        FieldPanel('embed_url'),
        FieldPanel('caption'),
        FieldPanel('show_video'),
        FieldPanel('date'),
    ]