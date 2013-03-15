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
#  RssRead 0.1
#  by Luca Francesca, 2013

import feedparser
import xml.etree.cElementTree as etree


class RssRead:
    """RssRead main method"""
    def __init__(self, fileName='config.xml'):
        self.fileName = fileName
        self.siteConf = {}
        self.NewsDict = {}
        self.tree = etree.parse(fileName)
        self.Config = self.tree.getroot()

    """Configuration loading method"""
    def loadConf(self):
        for child in self.Config:
            self.siteConf[child.find('name').text] = child.find('url').text

    """News loading method"""
    def loadNewsRss(self, site):
        self.feed = feedparser.parse(self.siteConf[site],
                                     agent='RssRead/0.1 +http://ciscoland.eu/')
        for news in self.feed.entries:
            self.NewsDict[news.title.encode('utf-8')] = news.link

    """News getting method"""
    def getNews(self):
        pass

    """Configuration site adding method"""
    def addSite(self, name, url):
        Site = etree.SubElement(self.Config, 'site')
        etree.SubElement(Site, 'name').text = name
        etree.SubElement(Site, 'url').text = url
        self.tree.write(self.fileName, encoding='utf-8')

    """Configuration site removing  method"""
    def removeSite(self, site):
        for Site in self.Config.findall('site'):
            if Site.find('name').text == site:
                self.Config.remove(Site)
        self.tree.write(self.fileName, encoding='utf-8')

# Testing


def main():
    rss = RssRead()
    rss.loadConf()
    rss.addSite('io', 'tu')
    rss.addSite('Not', 'ju')
    rss.removeSite('io')


if __name__ == '__main__':
    main()
