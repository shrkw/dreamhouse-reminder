#!/bin/env python
# encoding: UTF-8

from __future__ import division, print_function, absolute_import

import sys
import os
sys.path.append(os.getcwd())

from reminder import checker

import logging
from reminder.logger import handler
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

program_names = ("完成!ドリームハウス", "ローカル路線バス乗り継ぎの旅")

if __name__ == "__main__":
    logger.info("start")
    import time
    import calendar
    wday = time.gmtime().tm_wday
    if (wday == calendar.MONDAY or
       wday == calendar.THURSDAY):
        try:
            for name in program_names:
                checker.run(names)
        except Exception as e:
            logger.error('Error: ', exc_info=True)
    else:
        logger.info("was not executed, day of week: %i" % wday)
    logger.info("end")
