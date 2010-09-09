# -*- coding: utf-8 -*-
"""
Flask-Brevé
-----------

A Brevé_ templates loader for Flask_ applications.

.. _Flask: http://flask.pocoo.org/
.. _Brevé: http://breve.twisty-industries.com/

"""
from setuptools import setup


setup(
    name='Flask-Breve',
    version='0.1',
    url='http://github.com/dgerber/Flask-Breve',
    license='BSD',
    author='Daniel Gerber',
    author_email='',
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
