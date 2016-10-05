from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext as _build_ext

class build_ext(_build_ext):
    def finalize_options(self):
        _build_ext.finalize_options(self)
        # Prevent numpy from thinking it is still in its setup process:
        __builtins__.__NUMPY_SETUP__ = False
        import numpy
        self.include_dirs.append(numpy.get_include())

extensions = [
    Extension('pysupercluster',
        extra_compile_args=['-std=c++1y'],
        language='c++',
        depends=[
            'src/kdbush.hpp',
            'src/supercluster.hpp',
        ],
        sources=[
            'src/module.cpp',
            'src/supercluster.cpp',
        ],
    )
]

setup(name='pysupercluster',
      version='0.5',
      description='A fast geospatial point clustering module.',
      author='Jeremy Lainé',
      author_email='jeremy@getwemap.com',
      url='https://github.com/wemap/pysupercluster',
      cmdclass={'build_ext': build_ext},
      setup_requires=['numpy >= 1.7.0'],
      ext_modules=extensions,
)
