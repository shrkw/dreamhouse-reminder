#!/bin/env python
# coding:utf-8

import json
import requests

import logging
from .logger import handler
logger = logging.getLogger(__name__)
logger.addHandler(handler)

from .config import *  # noqa

class SlackNotifier:
    def __init__(self):
        self.url = SLACK_WEBHOOK_URL

    def notify(self, message):
        payload={"text": message}
        r = requests.post(self.url, data=json.dumps(payload))
        if r.status_code != 200:
            logger.warn("headers: %s" % (r.headers))
