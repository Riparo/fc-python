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
    long_description_content_type='text/markdown',

    url='https://github.com/Thoxvi/Fuck-Py-Functional',
    author='Thoxvi',
    author_email='A@Thoxvi.com',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='lambda function',

    packages=find_packages(exclude=['function_chain']),

    project_urls={
        'Source': 'https://github.com/Thoxvi/Fuck-Py-Functional',
    },
)
