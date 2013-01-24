from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(name='reimegard',
      version=version,
      description="tester2",
      long_description="""\
test""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='johan reimegard',
      author_email='johan.reimegard@scililfelab.se',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
