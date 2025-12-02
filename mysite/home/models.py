from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

from .blocks import (
    HeadingBlock,
    ParagraphBlock,
    ImageBlock,
    CtaBlock
)

class HomePage(Page):
    template = "home/home_page.html"

    body = StreamField([
        ('heading', HeadingBlock()),
        ('paragraph', ParagraphBlock()),
        ('image', ImageBlock()),
        ('cta', CtaBlock()),
    ], blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
