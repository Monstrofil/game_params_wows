#!/usr/bin/python
# coding=utf-8
from __future__ import print_function
from __future__ import unicode_literals

import argparse

from GameParams import GameParams

__author__ = "Aleksandr Shyshatsky"
__doc__ = "Command-line interface"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', metavar='FILE', type=str, nargs=1,
                        help='path to GameParams.data')
    parser.add_argument('--json', action='store_true', required=True,
                        help='show data as json')
    parser.add_argument('--by_id', action='store_true',
                        help='show data by id')

    namespace = parser.parse_args()
    if namespace.json:
        gp = GameParams()
        gp.load(namespace.file_path[0])
        print(gp.get_json())
    else:
        raise argparse.ArgumentTypeError('Use --json, other modes are not supported!')
