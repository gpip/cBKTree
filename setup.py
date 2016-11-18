from setuptools import setup, Extension

from Cython.Build import cythonize


setup(
    name='cbktree',
    version='0.1',
    description='bktree data structure',
    packages=['cbktree'],
    package_dir={"cbktree": "lib"},
    maintainer="Guilherme Polo",
    url="https://github.com/gpip/cBKTree",
    ext_modules=cythonize(Extension(
        "cbktree/cyHamDb",
        sources=["lib/cyHamDb.pyx"],
        libraries=["stdc++"],
        include_dirs=['lib'],
        language="c++",
        extra_compile_args=["-std=c++11", "-march=native", "-mtune=native", "-O3", "-mpopcnt"],
        extra_link_args=["-std=c++11", "-march=native", "-mtune=native", "-O3", "-mpopcnt"]
    ))
)
