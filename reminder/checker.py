#!/bin/env python
# encoding: UTF-8

import requests
from collections import namedtuple

from bs4 import BeautifulSoup

from .config import *  # noqa
from .notifier import Notifier

import logging
from .logger import handler
logger = logging.getLogger(__name__)
logger.addHandler(handler)

Schedule = namedtuple("Schedule", ["date", "time", "desc", "url"])


def check(q):
    url = "https://tv.yahoo.co.jp/search/category/"
    payload = {'a': 23, 'oa': 1, 'tv': 1, 'bsd': 1, 'cs': 1, 'q': q}
    r = requests.post(url, data=payload)
    soup = BeautifulSoup(r.content, "html.parser")
    cnt = soup.find_all("span", attrs={"class": "yjL"})[1]
    if int(cnt.text) is not 0:
        left = soup.find("div", attrs={"class": "leftarea"})
        if left is None:
            return None
        child = left.findChild('p')
        right = soup.find("div", attrs={"class": "rightarea"})
        return Schedule(child.text, child.nextSibling.nextSibling.text,
                        right.text, url)
    else:
        return None


def run(q):
    schedule = check(q)
    if schedule is not None:
        logger.info("found: %s" % q)
        notifier = Notifier.lookup("slack")
        notifier.notify("@%s %sの放送が予定されています。 %s %s %s \n %s" %
                        ("shrkwh", q, schedule.date, schedule.time,
                         schedule.url, schedule.desc))
    else:
        logger.info("not found: %s" % q)
