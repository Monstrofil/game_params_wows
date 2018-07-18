#!/usr/bin/python
# coding=utf-8
from __future__ import unicode_literals

from json import JSONEncoder

__author__ = "Aleksandr Shyshatsky"


class GameParamsJsonEncoder(JSONEncoder):
    """
    Encoder that helps to convert GameParams into json;
    """

    def default(self, o):
        return getattr(o, '__dict__', str(o))
