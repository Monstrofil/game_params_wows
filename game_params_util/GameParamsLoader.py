#!/usr/bin/python
# coding=utf-8
from __future__ import unicode_literals

import os
import pickle
import zlib
from StringIO import StringIO

from GameParamsExceptions import GameParamsLoaderDecompressError, GameParamsLoaderFileNotFound

__author__ = "Aleksandr Shyshatsky"


class GameParamsLoader(object):
    """
    Loader that gets path to GameParams.data file 
    and unpacks it.
    """

    def __init__(self, file_path):
        self.__file_path = file_path
        self.__decompressed_data = self.__decompress_data()

    def get_params(self):
        """
        Return GameParams object of current loaded GameParams.data;
        :rtype: dict[str, GameParams.GPData]
        """
        return pickle.loads(self.__decompressed_data)

    def __decompress_data(self):
        """
        Data in GameParams.data is compressed using zlib;
        This method decompresses data and returns string;
        :rtype: str 
        """
        io = self.__load_data()
        try:
            return zlib.decompress(io.read())
        except zlib.error as e:
            raise GameParamsLoaderDecompressError(e)

    def __load_data(self):
        """
        Load GameParams.data and reverse it's content
        Reverse is needed for further decompress;
        :rtype: StringIO 
        """
        if not os.path.exists(self.__file_path):
            raise GameParamsLoaderFileNotFound(self.__file_path)

        with open(self.__file_path, b'rb') as f:
            io = StringIO()
            io.write(f.read()[::-1])
            io.seek(0)
        return io
