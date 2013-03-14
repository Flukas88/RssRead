#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU LESSER GENERAL PUBLIC LICENSEG as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.
#    If not, see <http://www.gnu.org/copyleft/lesser.html>.
#
#  by Luca Francesca, 2013

from __future__ import print_function
import sys
import feedparser
import xml.etree.cElementTree as etree


siteConf = {}


def loadConf():
    tree = etree.parse('config.xml')
    root = tree.getroot()
    for child in root:
        siteConf[child.find('name').text] = child.find('url').text


def loadNewsRss(site):
        d = feedparser.parse(siteConf[site])
        for news in d.entries:
            print (news.title, '\n\t', '[ fonte: ', news.link, ']\n -- --\n')


def main():
    loadConf()
    try:
        loadNewsRss(sys.argv[1])
    except IndexError:
        print ('Non hai definito nessuna sorgente RSS!!\n \
                ====== Siti validi ====== ')
        for arg in siteConf:
            print (arg, '\n+-+-+')
    except KeyError:
        print ('Nome sito non valido!')


if __name__ == '__main__':
    main()
