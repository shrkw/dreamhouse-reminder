#!/bin/env python
# encoding: UTF-8

from __future__ import division, print_function, absolute_import
import argparse

import sys
import os
#sys.path.append(os.pardir)
sys.path.append(os.getcwd())

from reminder import checker

import logging
from reminder.logger import handler
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)


if __name__ == "__main__":
    logger.debug("start")
    parser = argparse.ArgumentParser(description='search TV program in Yahoo! TV schedule')
    parser.add_argument('query', nargs="?", help='TV program title', default='完成!ドリームハウス')
    args = parser.parse_args()

    try:
        checker.run(args.query)
    except Exception as e:
        logger.error('Error: ', exc_info=True)
    logger.debug("end")
