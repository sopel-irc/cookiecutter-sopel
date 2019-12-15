# coding=utf8
"""{{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}
"""
from __future__ import unicode_literals, absolute_import, division, print_function

from sopel import module


def configure(config):
    pass


def setup(bot):
    pass


@module.commands('helloworld')
def hello_world(bot, trigger):
    bot.say('Hello, world!')
