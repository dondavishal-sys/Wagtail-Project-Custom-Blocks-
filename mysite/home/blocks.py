from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class HeadingBlock(blocks.CharBlock):
    class Meta:
        template = "home/blocks/heading_block.html"
        icon = "title"
        label = "Heading"

class ParagraphBlock(blocks.TextBlock):
    class Meta:
        template = "home/blocks/paragraph_block.html"
        icon = "pilcrow"
        label = "Paragraph"

class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.CharBlock(required=False)

    class Meta:
        template = "home/blocks/image_block.html"
        icon = "image"
        label = "Image"

class CtaBlock(blocks.StructBlock):
    text = blocks.CharBlock()
    button_text = blocks.CharBlock()
    button_link = blocks.URLBlock()

    class Meta:
        template = "home/blocks/cta_block.html"
        icon = "plus"
        label = "CTA"
