from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='fc',
    version='0.0.3',
    description='Enables Python to be functionally chain-styled.',
    long_description=long_description,

    url='https://github.com/Thoxvi/Fuck-Py-Functional',
    author='Thoxvi',
    author_email='A@Thoxvi.com',

    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    keywords='lambda function',

    packages=find_packages(),
)
