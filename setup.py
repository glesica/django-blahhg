#!/usr/bin/env python

from distutils.core import setup

setup(
    name='django-blahhg',
    version='0.1.0',
    description='Simple embeddable blog for Django.',
    author='George Lesica',
    author_email='glesica@gmail.com',
    url='https://github.com/glesica/django-blahhg',
    packages=[
        'blahhg',
        'blahhg.templatetags',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary'
    ],
)
