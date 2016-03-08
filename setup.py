from os.path import join, dirname
from setuptools import setup

import image_fields

VERSION = (0, 0, 1)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

with open(join(dirname(__file__), 'README.rst')) as f:
    long_description = f.read().strip()

install_requires = [
    'Django>=1.8',
]
test_requires = [
    'nose',
    'coverage',
]

setup(
    name = 'django-image-fields',
    description = "Django image fields contains extra image fields for django framework",
    url = "https://github.com/MichalMaM/django-image-fields",
    long_description = long_description,
    version = image_fields.__versionstr__,
    author='Michal Dub',
    author_email='michalmam@centrum.cz',
    license='BSD',
    packages = ['image_fields'],
    zip_safe = False,
    include_package_data = True,
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Framework :: Django",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=install_requires,

    test_suite='nose.collector',
    tests_require=test_requires,
)
