# -*- coding: utf-8 -*-

from django import forms
from django.utils import simplejson as json
from django.conf import settings

# from https://bitbucket.org/schinckel/django-jsonfield/src/3f5db8f99fea/jsonfield/widgets.py
class JSONWidget(forms.Textarea):
    def render(self, name, value, attrs=None):
        if value is None:
            value = ""
        value = json.dumps(value, indent=2)
        return super(JSONWidget, self).render(name, value, attrs)
