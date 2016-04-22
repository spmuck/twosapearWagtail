from django.db import models
from django import forms
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet

@register_snippet
class Ingredient(models.Model):
    DEFAULT_SERVINGS_FORMAT_CHOICES = (
        ('quantity', 'Quantity'),
        ('volume', 'Volume'),
        ('weight', 'Weight'),
    )   
    name = models.CharField(max_length=100, unique=True)
    default_serving_format = models.CharField(choices=DEFAULT_SERVINGS_FORMAT_CHOICES,
        default='weight', max_length=10)
    serving_size_quantity = models.DecimalField(max_digits=10, decimal_places=1, blank=True)
    serving_size_volume = models.DecimalField(max_digits=10, decimal_places=1, blank=True)
    serving_size_weight = models.DecimalField(max_digits=10, decimal_places=1, blank=True)
    serving_quantity_description = models.CharField(max_length=100, unique=True, blank=True)
    calories = models.DecimalField(max_digits=10, decimal_places=1, default=0.0)
    calories_from_fat = models.DecimalField(max_digits=10, decimal_places=1, default=0.0)
    total_fat = models.DecimalField(max_digits=10, decimal_places=1, default=0.0)
    sat_fat = models.DecimalField(max_digits=10, decimal_places=1, default=0.0)
    poly_unsat_fat = models.DecimalField(max_digits=10, decimal_places=1, default=0.0)
    mono_unsat_fat = models.DecimalField(max_digits=10, decimal_places=1, default=0.0)
    cholesterol = models.DecimalField(max_digits=10, decimal_places=1, default=0.0)
    sodium = models.DecimalField(max_digits=10, decimal_places=1, default=0.0)
    potassium = models.DecimalField(max_digits=10, decimal_places=1, default=0.0)
    carbs = models.DecimalField(max_digits=10, decimal_places=1, default=0.0)
    fiber = models.DecimalField(max_digits=10, decimal_places=1, default=0.0)
    sugar = models.DecimalField(max_digits=10, decimal_places=1, default=0.0)
    protein = models.DecimalField(max_digits=10, decimal_places=1, default=0.0)
    vitamin_a = models.DecimalField(max_digits=10, decimal_places=1, default=0.0)
    vitamin_c = models.DecimalField(max_digits=10, decimal_places=1, default=0.0)
    calcium = models.DecimalField(max_digits=10, decimal_places=1, default=0.0)
    iron = models.DecimalField(max_digits=10, decimal_places=1, default=0.0)
    
    
        
    def __str__(self):
        return self.name

    panels = [
        FieldPanel('name'),
        FieldPanel('default_serving_format'),
        FieldPanel('serving_size_quantity'),
        FieldPanel('serving_size_volume'),
        FieldPanel('serving_size_weight'),
        FieldPanel('serving_quantity_description'),
        FieldPanel('calories'),
        FieldPanel('calories_from_fat'),
        FieldPanel('total_fat'),
        FieldPanel('sat_fat'),
        FieldPanel('poly_unsat_fat'),
        FieldPanel('mono_unsat_fat'),
        FieldPanel('cholesterol'),
        FieldPanel('sodium'),
        FieldPanel('potassium'),
        FieldPanel('carbs'),
        FieldPanel('fiber'),
        FieldPanel('sugar'),
        FieldPanel('protein'),
        FieldPanel('vitamin_a'),
        FieldPanel('vitamin_c'),
        FieldPanel('calcium'),
        FieldPanel('iron'),
    ]