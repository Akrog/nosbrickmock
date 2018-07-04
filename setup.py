#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

requirements = [
    'modulefaker',
]

test_requirements = [
]

dependency_links = [
    'http://github.com/akrog/modulefaker/tarball/master#egg=modulefaker',
]

description = "Mock of nos-brick"

setup(
    name='nos-brick',
    version='0.0.1',
    description=description,
    long_description=description,
    author="Gorka Eguileor",
    author_email='geguileo@redhat.com',
    url='https://github.com/akrog/cindermock',
    packages=[
        'nos_brick',
    ],
    package_dir={'nos_brick': 'nos_brick'},
    include_package_data=True,
    install_requires=requirements,
    dependency_links=dependency_links,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='nos_brick',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
