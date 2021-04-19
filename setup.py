#!/usr/bin/env python3
"""
Flask-NoFLoC sends the header

    Permissions-Policy: interest-cohort=()

with each request to opt websites out of FLoC.
See
    https://plausible.io/blog/google-floc#how-to-opt-out-of-floc-as-a-web-developer-set-a-permissions-policy
for more information.
"""

import re
from setuptools import setup

from pathlib import Path

version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                    Path('flask_nofloc.py').read_text(),
                    re.MULTILINE).group(1)
repository = 'https://github.com/shoeffner/Flask-NoFLoC'

install_requirements = ['Flask']
test_requirements = ['pytest']
docs_requirements = ['sphinx', 'pallets-sphinx-themes']
publish_requirements = ['wheel', 'twine']

setup(
    name='Flask-NoFLoC',
    version=version,
    description=__doc__,
    long_description=Path('README.rst').read_text(),
    long_description_content_type='text/x-rst',
    author='Sebatian Höffner',
    author_email='info@sebastian-hoeffner.de',
    url=repository,
    download_url='{}/tarball/{}'.format(repository, version),
    py_modules=['flask_nofloc'],
    include_package_data=True,
    platforms='any',
    python_requires=">= 3.6",
    install_requires=install_requirements,
    tests_require=test_requirements,
    extras_require={
        'test': test_requirements,
        'docs': docs_requirements,
        'pub': publish_requirements,
    },
    license='MIT',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=[
        'flask',
        'floc',
        'nofloc',
    ],
)
