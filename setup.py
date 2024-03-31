#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# from requirements import r

with open("requirements.txt") as f:
    requirements = [req.strip() for req in f.readlines()]


setup(name='ArticleParser',
      version='1.0',
      url='https://github.com/TheProjectsX/ArticleParser',
      description='Parse Articles from WEB via Search Query',
      author='TheProjectsX',
      author_email='',
      license='MIT',
      packages=[
          'articleparser'
      ],
      package_dir={'articleparser': 'articleparser'},
      install_requires=requirements,
      # Include additional files
      include_package_data=True,
      # Additional classifiers
      classifiers=[
          'Programming Language :: Python :: 3',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
      ],
      )
