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
    """RssRead is a class meant to read Rss/Atom feed and export them to the world"""
    def __init__(self, fileName='config.xml'):
        self.fileName = fileName
        self.siteConf = {}
        self.NewsFeed = []
        self.news = []
        self.tree = etree.parse(fileName)
        self.Config = self.tree.getroot()

    def loadConf(self):
        """Configuration loading method"""
        for child in self.Config:
            self.siteConf[child.find('name').text] = child.find('url').text

    def loadNewsRss(self, site):
        """News loading method"""
        self.feed = feedparser.parse(self.siteConf[site],
                                     agent='RssRead/0.1 +http://ciscoland.eu/')
        for news in self.feed.entries:
            newsStr = '<b>' + news.title + '<a href="' + news.link + '"></a></b><br />'
            newsStr = newsStr.encode('utf-8')
            self.news.append(newsStr)

    def getNews(self, site):
        """News getting method"""
        return self.news

    def addSite(self, name, url):
        """Configuration site adding method"""
        Site = etree.SubElement(self.Config, 'site')
        etree.SubElement(Site, 'name').text = name
        etree.SubElement(Site, 'url').text = url
        self.tree.write(self.fileName, encoding='utf-8')

    def removeSite(self, site):
        """Configuration site removing  method"""
        for Site in self.Config.findall('site'):
            if Site.find('name').text == site:
                self.Config.remove(Site)
        self.tree.write(self.fileName, encoding='utf-8')

# Testing


def main():
    rss = RssRead()
    rss.loadConf()
    rss.loadNewsRss('Ansa')
    news = rss.getNews('Ansa')
    print news


if __name__ == '__main__':
    main()
