#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals, absolute_import, division, print_function

import unittest

from sopel_modules.{{cookiecutter.module_name}} import {{cookiecutter.module_name}}

class Test{{cookiecutter.module_name|capitalize}}(unittest.TestCase):
    def setUp(self):
        pass

    def testSomething(self):
        pass
