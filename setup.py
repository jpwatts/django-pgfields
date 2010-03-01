from distutils.core import setup


setup(
    name='django-pgfields',
    version='0.1',
    description='Django model fields for PostgreSQL',
    author='Joel Watts',
    author_email='joel@joelwatts.com',
    url='http://github.com/jpwatts/django-pgfields',
    packages=[
        'pgfields',
        'pgfields.db',
        'pgfields.db.models',
        'pgfields.gis',
        'pgfields.gis.db',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
