# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def main():
	r = requests.get('http://esf.fang.com/house/w33/')
	soup = BeautifulSoup(r.text, "html.parser")
	print (soup.title.text)

if __name__ == '__main__':
    main()