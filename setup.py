"""pypi compatible setup module.

This setup is based on:
https://packaging.python.org/tutorials/distributing-packages/


"""
from setuptools import setup
from codecs import open
from os import path

import versioneer


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pybricks-api',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Pybricks',
    long_description=long_description,
    url='https://github.com/pybricks',
    author='Laurens Valk and David Lechner',
    author_email='laurens@pybricks.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='lego mindstorms ev3',
    python_requires='~=3.4',
    packages=['pybricks'],
)
