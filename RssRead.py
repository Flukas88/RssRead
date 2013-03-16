#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU LESSER GENERAL PUBLIC LICENSEG as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.
# If not, see <http://www.gnu.org/copyleft/lesser.html>.
#
# RssRead 0.11
# by Luca Francesca, 2013

import feedparser
import xml.etree.cElementTree as etree


class RssRead:
    """ Default config.xml or pass it a customized one as parameter. """
    def __init__(self, fileName='config.xml'):
        self._fileName = fileName
        self._siteConf = {}
        self._news = []
        self._tree = etree.parse(self._fileName)
        self._Config = self._tree.getroot()

    def loadConf(self):
        """Configuration loading method (first call of the class)"""
        self._siteConf = dict((child.find('name').text, child.find('url').text)
                              for child in self._Config)

    def loadNewsRss(self, site):
        """It *must* be followed by getNews(). Args are site."""
        self.feed = feedparser.parse(self._siteConf[site],
                                     agent='RssRead/0.11 +http://ciscoland.eu/')
        self._news = list('<a href="' + news.link.encode('utf-8') + '">' + news.title.encode('utf-8') + '</a><br />'
                          for news in self.feed.entries)

    def getNews(self):
        """News getting method.
        """
        return self._news

    def _addSite(self, name, url):
        """Configuration site adding method. The args are (name, url) """
        Site = etree.SubElement(self._Config, 'site')
        etree.SubElement(Site, 'name').text = name
        etree.SubElement(Site, 'url').text = url
        self._tree.write(self._fileName, encoding='utf-8')

    def _removeSite(self, site):
        """Configuration site removing method. Just give it the site name """
        for Site in self._Config.findall('site'):
            if Site.find('name').text == site:
                self._Config.remove(Site)
        self._tree.write(self._fileName, encoding='utf-8')

    def __sub__(self, site):
        self._removeSite(site)

    def __add__(self, cnf):
        self._addSite(cnf[0], cnf[1])
