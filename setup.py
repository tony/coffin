#!/usr/bin/env python
import os
import sys
from setuptools import setup, find_packages

sys.path.insert(0, os.path.join(os.path.dirname(__file__),))

setup(name='Coffin',
    version=".".join(map(str, __import__("coffin").__version__)),
    description='Jinja2 adapter for Django',
    author='Christopher D. Leary',
    author_email='cdleary@gmail.com',
    maintainer='David Cramer',
    maintainer_email='dcramer@gmail.com',
    url='http://github.com/coffin/coffin',
    packages=find_packages(),
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
    tests_require=['nose>=1.0', 'django_nose', 'django', 'Jinja2'],
    test_suite='runtests'
)
