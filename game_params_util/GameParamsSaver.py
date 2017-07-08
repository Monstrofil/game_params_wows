#!/usr/bin/python
# coding=utf-8
from __future__ import unicode_literals

import pickle
import zlib

__author__ = "Aleksandr Shyshatsky"


class GameParamsSaver(object):
    """
    Loader that saves GameParams into GameParams.data;
    """

    def __init__(self, game_params):
        """
        :type game_params: GameParams.GameParams
        """
        self.__game_params = game_params

    def save(self, file_path):
        """
        Convert GameParams into binary data 
        and save it into file;
        :type file_path: str 
        :rtype: None 
        """
        pickled = pickle.dumps(self.__game_params.data)
        compressed = zlib.compress(pickled, zlib.Z_BEST_COMPRESSION)
        binary_data = '%bin' + compressed[::-1]

        with open(file_path, 'wb') as f:
            f.write(binary_data)
