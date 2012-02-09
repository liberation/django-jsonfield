from django import forms
from django.utils import simplejson as json

from widgets import JSONWidget

# from https://bitbucket.org/schinckel/django-jsonfield/raw/3f5db8f99fea/jsonfield/forms.py
class JSONFormField(forms.CharField):
    widget = JSONWidget

    def clean(self, value):
        """
        The default is to have a TextField, and we will decode the string
        that comes back from this. However, another use of this field is
        to store a list of values, and use these in a MultipleSelect
        widget. So, if we have an object that isn't a string, then for now
        we will assume that is where it has come from.
        """
        if not value: 
            return value
        if isinstance(value, basestring):
            try:
                return json.loads(value)
            except Exception, exc:
                raise forms.ValidationError(u'JSON decode error: %s' % (unicode(exc),))
        else:
            return value