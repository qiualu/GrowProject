#!/usr/bin/python env
# coding: utf-8

import requests
from lxml import etree

DONE = set()
BAD = set()
SHIBAI = set()

def fetch(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        SHIBAI.add(url)
        return None
    elif url not in DONE:
        DONE.add(url)
        BAD.add(url)
    return resp.text
def parse(html):
    pass
def main():
    BAD.add('http://m.sohu.com')
    while True:
        li = list(BAD)
        if len(li) < 1:
            break
        for i in li:
            html = fetch(i)
            if html == None:
                continue
            parse(html)


if __name__ == '__main__':
    main()




