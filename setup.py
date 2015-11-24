#!/usr/bin/env python

from codecs import open
from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='goshstore',
    version='0.1.0',
    description='Django get-or-set hstore field',
    long_description=long_description,
    url='https://github.com/conanfanli/goshstore',
    packages=find_packages(exclude=['doc', 'tests*']),
    install_requires=['django>=1.8,<1.8.9'],
    extras_require={
        'dev': ['psycopg2==2.6.1']
    },
    classifiers=[
        'Development Status :: 3 - Alpha',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.4'
    ],
    keywords='django hstore postgres',
    author='Conan Fan Li',
    author_email='conanlics@gmail.com',
    license='MIT',
)
