
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Kruskal',
    version='1.0',

    description='Library for Kruskal's algorithm',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/NKPyo/kruskal/',

    # Author details
    author='ninad patil',
    author_email='ninad@minerva.kgi.edu',

    # Choose your license
    license='MIT',

    
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ],

    keywords='kruskal minimum spanning tree',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['networkx'],
    entry_points={
        'console_scripts': [
            'kruskal=kruskal:kruskal',
        ],
    },
)
