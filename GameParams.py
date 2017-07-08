#!/usr/bin/python
# coding=utf-8
# Mock for real data structures in WorldOfWarships game.
# Used during unpickling process;
from __future__ import unicode_literals

import json

from game_params_util.GameParamsJsonEncoder import GameParamsJsonEncoder
from game_params_util.GameParamsLoader import GameParamsLoader
from game_params_util.GameParamsSaver import GameParamsSaver

__author__ = "Aleksandr Shyshatsky"


class TypeInfo(object):
    """
    Restored from in-game objects;
    Other objects may contain some other data, 
    but all of them contain following fields:
    """

    def __init__(self):
        self.type = ''


class GPData(object):
    def __init__(self):
        """
        Restored from in-game objects;
        Other objects may contain some other data, 
        but all of them contain following fields:
        """
        self.id = -1  # type: long
        self.typeinfo = None  # type: TypeInfo


class GameParams(object):
    """
    Copy of in-game class GameParams;
    Data can be accessed two ways: 
    >>> GameParams(...).data
    {'PBPA009_152MM_AP_100LBS': <GameParams.GPData object at ...>, ...}
    >>> GameParams(...).dataById
    {1233434534L: <GameParams.GPData object at ...>, ...}
    
    Usage:
    gp = GameParams().load('/path/to/GameParams.data')
    gp.save('/path/where/to/save/new/GameParams.data')
    """

    def __init__(self):
        """
        Initialize properties;
        """
        self.data = {}
        self.dataById = {}

    def save(self, file_path='GameParams.data'):
        """
        Save GameParams into GameParams.data file;
        Client should be able to read such modified file;
        :rtype: None 
        """
        GameParamsSaver(self).save(file_path)

    def load(self, file_path='GameParams.data'):
        """
        Save GameParams into GameParams.data file;
        Client should be able to read such modified file;
        :rtype: GameParams 
        """
        self.data = GameParamsLoader(file_path).get_params()
        self.dataById = {item.id: item for item in self.data.itervalues()}

        return self

    def get_json(self, by_id):
        """
        Not an in-game method, but new one added;
        :type by_id: bool
        :rtype: str 
        """
        return json.dumps(self.dataById if by_id else self.data, cls=GameParamsJsonEncoder, ensure_ascii=False)
