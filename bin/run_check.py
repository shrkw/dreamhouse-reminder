#!/bin/env python
# encoding: UTF-8

from __future__ import division, print_function, absolute_import
import argparse

import sys
import os
#sys.path.append(os.pardir)
sys.path.append(os.getcwd())

from reminder import checker

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='search TV program in Yahoo! TV schedule')
    parser.add_argument('query', nargs="?", help='TV program title', default='完成!ドリームハウス')
    args = parser.parse_args()
    checker.run(args.query)
