# -*- coding: utf-8 -*-
"""
Flask-Brevé
-------------

A Brevé templates loader for Flask applications.

Links
`````
* `Flask http://flask.pocoo.org/`_
* `Brevé http://breve.twisty-industries.com/`_
* `documentation <http://packages.python.org/Flask-Breve>`_

"""
from setuptools import setup


setup(
    name='Flask-Breve',
    version='0.1',
    url='<enter URL here>',
    license='BSD',
    author='Daniel Gerber',
    author_email='your-email-here@example.com',
    description='Breve templating with Flask',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask', 
        'Breve'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
