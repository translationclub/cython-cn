# -*- coding: utf-8 -*-

from distutils.core import setup

from Cython.Build import cythonize


setup(
    name='Cintegrate',
    ext_modules=cythonize('cintegrate.pyx'),
)
