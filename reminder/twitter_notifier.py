#!/bin/env python
# coding:utf-8

from TwitterAPI import TwitterAPI

import logging
from .logger import handler
logger = logging.getLogger(__name__)
logger.addHandler(handler)

from .config import *  # noqa

class TwitterNotifier:
    def __init__(self):
        self.client = TwitterAPI(TWI_CONSUMER_KEY,
                         TWI_CONSUMER_SECRET,
                         TWI_ACCESS_TOKEN_KEY,
                         TWI_ACCESS_TOKEN_SECRET)

    def notify(self, message):
        r = self.client.request('statuses/update', {'status': message})
        logger.info("twitter response code: %s" % (r.status_code))
        logger.debug("twitter response text: %s" % (r.text))
        if r.status_code != 200:
            logger.warn("headers: %s" % (r.headers))
