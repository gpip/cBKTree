from setuptools import setup, Extension

from Cython.Build import cythonize

version = None
for line in open('./lib/version.py'):
    if line.startswith('__version__'):
        version = line.split('=')[1].strip()[1:-1]  # drop quotes.
        break
else:
    raise Exception("Could not find package version")


setup(
    name='cbktree',
    version=version,
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
