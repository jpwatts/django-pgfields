import uuid

import psycopg2.extras

from django import forms
from django.db import models


__all__ = ('CharField', 'EmailField', 'SlugField', 'URLField', 'UUIDField')


class CharField(models.Field):
    def formfield(self, **kwargs):
        defaults = {'widget': forms.TextInput}
        defaults.update(kwargs)
        return super(CharField, self).formfield(**defaults)

    def db_type(self, connection=None):
        if self.max_length:
            return 'varchar(%s)' % self.max_length
        return 'text'


class EmailField(CharField):
    def formfield(self, **kwargs):
        defaults = {'form_class': forms.EmailField}
        defaults.update(kwargs)
        return super(EmailField, self).formfield(**defaults)


class SlugField(CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('db_index', True)
        super(SlugField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.SlugField}
        defaults.update(kwargs)
        return super(SlugField, self).formfield(**defaults)


class URLField(CharField):
    def __init__(self, verbose_name=None, name=None, verify_exists=True, **kwargs):
        self.verify_exists = verify_exists
        super(URLField, self).__init__(verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.URLField, 'verify_exists': self.verify_exists}
        defaults.update(kwargs)
        return super(URLField, self).formfield(**defaults)


# Register the adapter so we can use UUID objects.
psycopg2.extras.register_uuid()

class UUIDField(CharField):
    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('default', uuid.uuid4)
        kwargs.setdefault('editable', not kwargs.get('primary_key', False))
        super(UUIDField, self).__init__(*args, **kwargs)

    def db_type(self, connection=None):
        return 'uuid'

    def get_db_prep_value(self, value):
        return self.to_python(value)
    
    def to_python(self, value):
        if not value:
            return None
        if not isinstance(value, uuid.UUID):
            value = uuid.UUID(value)
        return value
