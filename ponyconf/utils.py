from django.db import models
from django.utils.html import mark_safe

import bleach
from markdown import markdown


class PonyConfModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def markdown_to_html(md):
    html = markdown(md)
    allowed_tags = bleach.ALLOWED_TAGS + ['p', 'pre', 'span'] + ['h%d' % i for i in range(1, 7)]
    html = bleach.clean(html, tags=allowed_tags)
    return mark_safe(html)
