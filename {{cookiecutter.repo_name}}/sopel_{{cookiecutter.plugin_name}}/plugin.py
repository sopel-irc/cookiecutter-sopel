"""{{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}
"""
from __future__ import annotations

from sopel import plugin


def configure(config):
    pass


def setup(bot):
    pass


@plugin.command('helloworld')
def hello_world(bot, trigger):
    bot.say('Hello, world!')
