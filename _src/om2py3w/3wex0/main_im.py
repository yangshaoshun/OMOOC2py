#!/usr/bin/python           # This is client.py file
# -*- coding: utf-8 -*-
"""

Usage:
  main.py (s|c)
  main.py (-h|--help)
  main.py --version

Options:
  -h --help     Show this screen
  --version     Show version

"""

from docopt import docopt
import socket
import serim
from serim import server
import clim
from clim import client

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Mydaily3.0')
    if arguments['s']:  #arguments 是个字典，所以使用索引
        server()
    if arguments['c']:
        client()