# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from lxml import html, etree
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def main():
    r = requests.get('http://esf.fang.com/house/w33/')
    page = etree.HTML(r.content.decode('utf-8','ignore'))

#    tree = html.fromstring(r.content)
#    print tree
    title = page.xpath('//*[@id="list_D03_01"]/dd/p[1]/a/text()')
    print title
''

if __name__ == '__main__':
    main()