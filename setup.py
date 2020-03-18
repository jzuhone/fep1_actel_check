#!/usr/bin/env python
from setuptools import setup

entry_points = {'console_scripts': 'fep1_actel_check = fep1_actel_check.fep1_actel_check:main'}

setup(name='fep1_actel_check',
      packages=["fep1_actel_check"],
      use_scm_version=True,
      setup_requires=['setuptools_scm', 'setuptools_scm_git_archive'],
      description='ACIS Thermal Model for FEP1 Actel Temperatures',
      author='John ZuHone',
      author_email='jzuhone@gmail.com',
      url='http://github.com/acisops/fep1_actel_check',
      include_package_data=True,
      entry_points=entry_points,
      )
