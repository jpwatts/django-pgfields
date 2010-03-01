===============
django-pgfields
===============

This is collection of Django model field subclasses that take advantage of
PostgreSQL's column types.

``CharField``, ``EmailField``, ``SlugField`` and ``URLField`` make the
``max_length`` argument optional, but otherwise work like the standard Django
fields.  When ``max_length`` isn't specified, the ``TEXT`` column type is
used.  See the `PostgreSQL documentation`_ for more on
``TEXT`` vs. ``VARCHAR``.

``UUIDField`` uses the ``UUID`` column type and is represented in Python as a
``uuid.UUID`` instance.

Usage
-----

This package mimics GeoDjango by providing ``pgfields.db.models`` as a
drop-in replacement for ``django.db.models``.  In the same style,
``pgfields.gis.db.models`` replaces ``django.contrib.gis.db.models``.

::

    from pgfields.db import models

    class Person(models.Model):
        id = models.UUIDField("ID", primary_key=True)
        name = models.CharField("name")


.. _`PostgreSQL documentation`: http://www.postgresql.org/docs/current/interactive/datatype-character.html
