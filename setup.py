#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='goshstore',
    version='0.1',
    description='Django get-or-set hstore field',
    url='https://github.com/conanfanli/goshstore',
    packages=find_packages(),
    install_requires=['django>=1.8,<1.8.9'],
    classifiers=[
        'Programming Language :: Python :: 3.4'
    ]
)
