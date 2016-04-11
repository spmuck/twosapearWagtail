from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet

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
    
    def __str__(self):
        return self.title

    panels = [
        FieldPanel('title'),
        ImageChooserPanel('image'),
        FieldPanel('embed_url'),
        FieldPanel('caption'),
    ]