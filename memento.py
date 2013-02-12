#!/usr/local/bin/python

import sys
from os.path import *
from subprocess import call
import string

# Change the constants below to match your system
USERNAME = 'tir'
GLOBHIST = '/home/%s/.elinks/globhist' % USERNAME
PATH = '/home/%s/memento/data/' % USERNAME
ALLOWEDCHARS = string.ascii_letters + string.digits + ' -_'

def get_links():
    with open(GLOBHIST,  'r') as historyfile:
        return historyfile.readlines()

def get_site_texts():
    linklist = get_links()
    for link in linklist:
        title, url, timestamp = link.split('\t')
        timestamp = timestamp.strip()

        # Strip out obnoxious characters
        title = ''.join(c for c in title if c in ALLOWEDCHARS)

        dumpfile = '%s%s-%s' % (PATH, timestamp, title)
        if (not isfile(dumpfile)):
            call ('lynx --dump "%s" > "%s"' % (url, dumpfile), shell=True)

if __name__ == '__main__':
    get_site_texts()
