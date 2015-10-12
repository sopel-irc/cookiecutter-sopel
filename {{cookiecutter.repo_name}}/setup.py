# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import sys
from setuptools import setup, find_packages


if __name__ == '__main__':
    print('Sopel does not correctly load modules installed with setup.py '
          'directly. Please use "pip install .", or add {}/sopel_modules to '
          'core.extra in your config.'.format(
              os.path.dirname(os.path.abspath(__file__))),
          file=sys.stderr)

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('NEWS') as history_file:
    history = history_file.read()

with open('requirements.txt') as requirements_file:
    requirements = [req for req in requirements_file.readlines()]

with open('dev-requirements.txt') as dev_requirements_file:
    dev_requirements = [req for req in dev_requirements_file.readlines()]


setup(
    name='sopel_modules.{{cookiecutter.module_name}}',
    version='{{cookiecutter.version}}',
    description='{{cookiecutter.project_short_description}}',
    long_description=readme + '\n\n' + history,
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    url='http://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}',
    packages=find_packages('.'),
    namespace_packages=['sopel_modules'],
    include_package_data=True,
    requires=requirements,
    tests_require=dev_requirements,
    test_suite='tests',
    license='Eiffel Forum License, version 2',
)
