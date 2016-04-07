from django import forms

from wagtail.wagtailcore.blocks import FieldBlock

class ImageAlignmentChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('left', 'Wrap left'), ('right', 'Wrap right'), ('mid', 'Mid width'), ('full', 'Full width'),
    ))