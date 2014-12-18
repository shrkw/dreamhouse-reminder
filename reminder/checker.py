#!/bin/env python
# encoding: UTF-8

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from TwitterAPI import TwitterAPI

from .config import * # noqa

def check(q):
    '''
    '''
    b = "http://tv.yahoo.co.jp/search/?q=%s&g=&Submit.x=0&Submit.y=0"
    res = BeautifulSoup(urllib.request.urlopen(b % urllib.parse.quote_plus(q)))
    cnt = res.find_all("span", attrs={"class" : "yjL"})[1]
    if int(cnt.text) is not 0:
        return True
    else:
        return False


def tweet(s):
    api = TwitterAPI(TWI_CONSUMER_KEY,
                     TWI_CONSUMER_SECRET,
                     TWI_ACCESS_TOKEN_KEY,
                     TWI_ACCESS_TOKEN_SECRET)
    r = api.request('statuses/update', {'status': s})
    if r.status_code != 200:
        print(r.status_code)
        print(r.headers)
        print(r.text)


def run(q):
    program = check(q)
    import time
    if program:
        tweet("@shrkwh %sの放送が予定されています。 %i" % (q, int(time.mktime(time.gmtime()))))
    else:
        tweet("@shrkwh %sの放送が見つかりませんでした。 %i" % (q, int(time.mktime(time.gmtime()))))
