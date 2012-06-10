#!/usr/bin/env python
#coding: utf-8

from distutils.core import setup, Extension

setup(
    ext_modules = [
    Extension(
        '_geohash', ['geohash.i', 'libgeohash/geohash.c'],
        swig_opts=['-modern'],
        library_dirs=[],
        libraries=[])
    ]
)
