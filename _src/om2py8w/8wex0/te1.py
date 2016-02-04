# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

def main():
    r = requests.get('http://esf.fang.com/house/w33/')
    soup = BeautifulSoup(r.text, "html.parser")
#    print soup.find(id = 'list_D03_01')
#    print soup.findAll(id=re.compile("^list_D\d+"))
#    for tag in soup.find_all(re.compile("^dl")):
#        print tag.attrs
#    print soup.find_all("p", "title")
#    list = ['list_D03_01','list_D03_02']
#    for id in list:
#        print soup.find_all(id = id)
    select = soup.find_all("dd", class_= "info rel floatr")
#    select = soup.select("body div div div div dl dd")
    reg1 = re.compile('</?\w+[^>]*>')
    for line in select:
        line_list = line.encode("utf-8")
        line_content = reg1.sub('',line_list)
        print line_content.strip()

if __name__ == '__main__':
    main()