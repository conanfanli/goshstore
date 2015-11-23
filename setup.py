#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='goshstore',
    version='0.1.0dev1',
    description='Django get-or-set hstore field',
    url='https://github.com/conanfanli/goshstore',
    packages=find_packages(exclude=['doc', 'tests*']),
    install_requires=['django>=1.8,<1.8.9'],
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
