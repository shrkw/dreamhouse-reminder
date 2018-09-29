#!/bin/env python
# coding:utf-8

import os

TWI_CONSUMER_KEY = os.environ.get("TWI_CONSUMER_KEY", "")
TWI_CONSUMER_SECRET = os.environ.get("TWI_CONSUMER_SECRET", "")
TWI_ACCESS_TOKEN_KEY = os.environ.get("TWI_ACCESS_TOKEN_KEY", "")
TWI_ACCESS_TOKEN_SECRET = os.environ.get("TWI_ACCESS_TOKEN_SECRET", "")
SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL", "")
