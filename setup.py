#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import pydjax

setup(
    name = 'pydjax',
    version = "0.1",
    description = "Easily Use MathJax with Django without any hassel",
    long_description = "",
    keywords = 'django, mathjax, djax',
    author = 'Palash Bauri',
    author_email = 'palashbauri1@gmail.com',
    url = 'https://github.com/bauripalash/djax',
    license = 'MIT',
    include_package_data = True,
    packages = find_packages(),
    classifiers = [
        "Programming Language :: Python",
        'Development Status :: Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
