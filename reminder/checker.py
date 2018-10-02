#!/bin/env python
# encoding: UTF-8

import urllib.request
import urllib.parse
from collections import namedtuple

from bs4 import BeautifulSoup

from .config import *  # noqa
from .notifier import Notifier

import logging
from .logger import handler
logger = logging.getLogger(__name__)
logger.addHandler(handler)

Schedule = namedtuple("Schedule", ["date", "time", "url"])


def check(q):
    b = "https://tv.yahoo.co.jp/search/?q=%s&g=&Submit.x=0&Submit.y=0"
    url = b % urllib.parse.quote_plus(q)
    res = BeautifulSoup(urllib.request.urlopen(url), "html.parser")
    cnt = res.find_all("span", attrs={"class": "yjL"})[1]
    if int(cnt.text) is not 0:
        left = res.find("div", attrs={"class": "leftarea"})
        child = left.findChild('p')
        return Schedule(child.text, child.nextSibling.nextSibling.text, url)
    else:
        return None


def run(q):
    schedule = check(q)
    if schedule is not None:
        logger.info("found: %s" % q)
        notifier = Notifier.lookup("slack")
        notifier.notify("@%s %sの放送が予定されています。 %s %s %s" %
                        ("shrkwh", q, schedule.date, schedule.time,
                         schedule.url))
    else:
        logger.info("not found: %s" % q)
