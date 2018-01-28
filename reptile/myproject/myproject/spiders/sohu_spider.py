#!/usr/bin/python env
# coding: utf-8

import requests
from lxml import etree
from threading import Thread
from queue import Queue

DONE = set()
BAD = set()
TODO = Queue()


def fetch(url):
    print('Fetching %s' % (url))

    try:
        resp = requests.get(url)
    except Exception as e:
        print('Error: %s' % e)
        return ''

    if resp.status_code != 200:
        BAD.add(url)
    else:
        DONE.add(url)
    return resp.text


def check_url(url):
    '''check url'''
    # 规范化
    if url.startswith('//'):
        url = 'http:%s' % url

    if url.startswith('/'):
        url = 'http://m.sohu.com%s' % url

    # 域名检查
    if '.m.sohu.com' not in url and '//m.sohu.com' not in url:
        return

    # 去重
    if url not in DONE and url not in BAD:
        return url


def parse(html):
    try:
        doc = etree.HTML(html)
    except Exception as e:
        print(e)
        return ''

    if doc is None:
        return []

    urls = doc.xpath('//a/@href')
    res = []
    for url in urls  :
        u = check_url(url)
        if u is not None:
            res.append(u)
    return res


def handle_urls():
    pass


def main():
    TODO.put('http://m.sohu.com')
    thread_pool = []
#
    for i in range(1000):
        t = Thread(target=i)
        t.setDaemon(True)
        t.start()
        thread_pool.append()

    # 等待所有线程退出
    for t in thread_pool:
        t.join()


if __name__ == '__main__':
    main()
