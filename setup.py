#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import path
import sys

from setuptools import setup, find_packages


def read(file):
    """ Reads and returns as a string the contents of a file.

    Parameters
    ----------
    file : str
        Path to the file to be read, relative to the directory where setup.py is
        located

    Returns
    -----
    output : str
        The contents of `file`.

    """
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, file), encoding='utf-8') as f:
        output = f.read()
    return output


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    package_name = 'zzw_projects'
    package_version = '0.1'
    homepage_url = 'https://github.com/williamscales/zzw_projects'
    package_author = 'William Scales'
    package_author_email = 'william@wscales.com'
    license = 'Apache Software License'
    short_description = 'ZZW projects page type for Mezzanine'
    long_description = read('README.rst')
    required = [
        'Django==1.7.1',
        'Mezzanine==3.1.10',
    ]
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    keywords = 'mezzanine theme'

    setup(
        name=package_name,
        version=package_version,
        description=short_description,
        long_description=long_description,
        url=homepage_url,
        author=package_author,
        author_email=package_author_email,
        license=license,
        platforms='OS Independent',
        classifiers=classifiers,
        keywords=keywords,
        packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
        install_requires=required,
    )

if __name__ == '__main__':
    sys.exit(main())
