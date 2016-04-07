from wagtail.wagtailcore.blocks import (TextBlock, StructBlock, StreamBlock,
                                        FieldBlock, CharBlock, RichTextBlock, 
                                        RawHTMLBlock, ListBlock)
from wagtail.wagtailimages.blocks import ImageChooserBlock
from .imagealignmentchoiceblock import ImageAlignmentChoiceBlock
from .imageformatchoiceblock import ImageFormatChoiceBlock

class TimedImageSeriesBlock(StructBlock):
    id = CharBlock(label = "ID MUST BE UNIQUE", default="01")
    images = ListBlock(ImageChooserBlock(label="Image", icon="image"))
    width = CharBlock(label = "Image Width")
    height = CharBlock(label = "Image Height")
    interval = CharBlock(label = "Interval in seconds")
    format = ImageFormatChoiceBlock(label = "Image Base Format", default="square_md")
    alignment = ImageAlignmentChoiceBlock()