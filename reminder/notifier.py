#!/bin/env python
# coding:utf-8

from .slack_notifier import SlackNotifier
from .twitter_notifier import TwitterNotifier


class Notifier:
    @classmethod
    def lookup(cls, type):
        type = type.lower()
        if type == "twitter":
            return TwitterNotifier()
        elif type == "slack":
            return SlackNotifier()
        else:
            return SlackNotifier()
