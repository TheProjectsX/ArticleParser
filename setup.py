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
          'parser'
      ],
      include_package_data=True,
      install_requires=requirements,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ]
      )
