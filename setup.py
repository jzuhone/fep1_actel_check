#!/usr/bin/env python
from setuptools import setup
from fep1_actel_check import __version__

entry_points = {'console_scripts': 'fep1_actel_check = fep1_actel_check.fep1_actel_check:main'}

url = 'https://github.com/acisops/fep1_actel_check/tarball/{}'.format(__version__)

setup(name='fep1_actel_check',
      packages=["fep1_actel_check"],
      version=__version__,
      description='ACIS Thermal Model for FEP1 Actel Temperatures',
      author='John ZuHone',
      author_email='jzuhone@gmail.com',
      url='http://github.com/acisops/fep1_actel_check',
      download_url=url,
      include_package_data=True,
      classifiers=[
          'Intended Audience :: Science/Research',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.5',
      ],
      entry_points=entry_points,
      )
