"""Packaging settings."""

import os
import subprocess

from setuptools import Command, find_packages, setup

from prototag import __version__


PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
README_PATH = os.path.join(PROJECT_DIR, 'README.md')

with open(README_PATH) as file:
    LONG_DESC = file.read()


class RunTests(Command):
    """Run all tests."""
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = subprocess.call(['py.test'])
        raise SystemExit(errno)


setup(
    name='ptag',
    version=__version__,
    license='MIT',
    description='A small cli tool to filter plain text files by header tags.',
    long_description=LONG_DESC,
    url='https://github.com/flxbe/prototag',
    author='Felix Bernhardt',
    author_email='felix.bernhardt@mailbox.org',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Topic :: Utilities',
        'Environment :: Console',

        'License :: OSI Approved :: MIT License',

        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='cli',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['docopt', 'yaml'],
    extras_require={
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points={
        'console_scripts': [
            'ptag=prototag:main',
        ],
    },
    python_requires='>=3',
    cmdclass={'test': RunTests},
)
