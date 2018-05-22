import os
from setuptools import setup, find_packages

setup(
    name='fc',
    version='0.1.5',
    description='Enables Python to be functionally chain-styled.',
    long_description=open(os.path.join(os.path.dirname(__file__),
                                       'README.md')).read(),
    long_description_content_type="text/markdown",
    python_requires='>=3.4',
    url='https://github.com/Thoxvi/Function-Chain-Python',
    author='Thoxvi',
    author_email='A@Thoxvi.com',

    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    keywords='lambda function',

    packages=["fc"],
)
