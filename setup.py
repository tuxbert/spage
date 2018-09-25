#!/usr/bin/env python
# coding=utf-8

from setuptools import setup


package_name = 'spage'
filename = f'{package_name}.py'


def get_version():
    import ast

    with open(filename) as input_file:
        for line in input_file:
            if line.startswith('__version__'):
                return ast.parse(line).body[0].value.s


def get_long_description():
    try:
        with open('README.md', 'r') as f:
            return f.read()
    except IOError:
        return ''


setup(
    name=package_name,
    version=get_version(),
    author='tuxbert',
    author_email='elliotpatonsimpson@gmail.com',
    description='SPAGE',
    url='https://github.com/tuxbert/spage',
    long_description=get_long_description(),
    packages=[package_name],
    entry_points={
        'console_scripts': [
            'spage = spage:spage'
        ]
    },
    license='License :: OSI Approved :: MIT License',
)
