# -*- coding: utf-8 -*-

__author__ = 'Markus Günther <markus.guenther@gmail.com>'
__license__ = "MIT License"

from setuptools import setup

with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")

classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: End Users/Desktop',
               'Programming Language :: Python :: 2.7',
               'Topic :: Utilities',
               'Environment :: Console']

setup(
    name = '',
    version = '0.1.0',
    author = 'Markus Günther',
    author_email = 'markus.guenther@gmail.com',
    description = 'PDF page extraction utility which provides a simple CLI-based frontend for pdftk',
    long_description = '',
    license = 'MIT License',
    keywords = 'pdftk pdf extract',
    url = 'http://www.habitat47.de',
    packages = ['pdfextract'],
    entry_points = {
        "console_scripts": ['pdfextract = pdfextract.pdfextract:main']
    })