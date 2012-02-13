# -*- coding: utf-8 -*-

from django import forms
from django.utils import simplejson as json
from django.conf import settings

# from https://bitbucket.org/schinckel/django-jsonfield/src/3f5db8f99fea/jsonfield/widgets.py
class JSONWidget(forms.Textarea):
    def render(self, name, value, attrs=None):
        if value is None:
            value = ""
        if not isinstance(value, basestring):
            # If the value is already in JSON format, we need to dump it into
            # a string. Don't do it if the value is already a string though! 
            value = json.dumps(value, indent=2)
        return super(JSONWidget, self).render(name, value, attrs)
