# -*- coding: utf-8 -*-

from distutils.core import setup

from Cython.Build import cythonize


setup(
    name='Integrate',
    ext_modules=cythonize('integrate.pyx'),
)
