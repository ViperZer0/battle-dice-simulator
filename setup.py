from setuptools import setup
from Cython.Build import cythonize

setup(
        name="simulator",
        version="0.0.1",
        ext_modules=cythonize("run.pyx")
        )
