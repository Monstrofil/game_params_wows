#!/usr/bin/python
# coding=utf-8
__author__ = "Aleksandr Shyshatsky"


class GameParamsLoaderErrorBase(Exception):
    pass


class GameParamsLoaderDecompressError(GameParamsLoaderErrorBase):
    pass


class GameParamsLoaderFileNotFound(GameParamsLoaderErrorBase):
    pass
