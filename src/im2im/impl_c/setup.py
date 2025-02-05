# setup.py
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("c_util.pyx", language_level="3")
)
