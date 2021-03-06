# -*- coding: UTF-8 -*-

from django import template
from django.utils.safestring import mark_safe
from django.utils.html import escape
from django.utils import simplejson#

from mathics.doc.doc import escape_html

register = template.Library()

@register.filter
def link(object, ajax):
    if object:
        href = object.href(ajax)
        return mark_safe('<a href="%s">%s</a>' % (escape(href), object.get_title_html()))
    else:
        return ''
    
@register.filter
def js(data):
    return mark_safe(simplejson.dumps(data))