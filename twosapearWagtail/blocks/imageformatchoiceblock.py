from django import forms

from wagtail.wagtailcore.blocks import FieldBlock

class ImageFormatChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('square_md', 'Square Medium Res - 400 x 400'), ('rect_lg', 'Rectangle Medium Res - 600x400'),
    )) 