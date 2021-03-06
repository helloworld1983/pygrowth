#!/usr/bin/env python

from setuptools import setup, find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name='pygrowth',
    version='0.0.2',
    url='https://github.com/growth-team/pygrowth',
    author='growth-team',
    author_email='teruaki.enoto@gmail.com',
    maintainer='Teru Enoto',
    maintainer_email='teruaki.enoto@gmail.com',
    description='Python package for public data analyses from the GROWTH collaboratoin.',
    long_description=open('README.md').read(),
    packages=find_packages(exclude=['tests*']),
    # packages=['pygrowth','pygrowth.general'],
    install_requires=_requires_from_file('requirements.txt'),
    test_requires=_requires_from_file('requirements.txt'),
    # Command-line interface
    entry_points={
        'console_scripts': ['eventfile=pygrowth.cli.eventfile:main']},
    test_suite="tests",
    license='MIT'
)
