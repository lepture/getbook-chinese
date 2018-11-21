#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from getbook_chinese import __version__ as version
from getbook_chinese import __homepage__ as homepage


def fread(filename):
    with open(filename) as f:
        return f.read()


install_requirements = ['getbook']


setup(
    name='getbook-chinese',
    version=version,
    author='Hsiaoming Yang',
    author_email='me@lepture.com',
    url=homepage,
    packages=['getbook_chinese'],
    entry_points={
        'getbook.parsers': [
            'dajia = getbook_chinese.dajia:DajiaParser'
        ],
    },
    description='Extra parsers of Chinese websites for getbook.',
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    long_description=fread('README.rst'),
    license='GNU AGPLv3+',
    install_requires=['getbook'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
