# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

def main():
    r = requests.get('http://esf.fang.com/house/w33/')
    soup = BeautifulSoup(r.text, "html.parser")
    li = soup.find(id = "list_D03_24")  # 查找网页中的某一间房
    # 去除 html 标签
    reg1 = re.compile('</?\w+[^>]*>')
    content = reg1.sub('',li.prettify())
    # 去除多余空行
#    blank_line = re.compile('\n+')
#    content = blank_line.sub('\n',content)
    content = content.strip()
    blank = re.compile('\n+')
    content = blank.sub('  ',content)
    print content

if __name__ == '__main__':
    main()