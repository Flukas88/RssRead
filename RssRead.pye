#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
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
# by Luca Francesca, 2016

from __future__ import absolute_import
from __future__ import print_function
import feedparser
import re
import json
import time
import xml.etree.cElementTree as etree
import RssConfValidate as validate


class SiteError(Exception):
    """ Site error Exception Class """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class ConfigurationError(Exception):
    """ Configuration Exception Class """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class FormatError(KeyError):
    """ Output Format  Exception Class """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class RssRead:
    """ Default config.xml or pass it a customized one as parameter. """
    def __init__(self, fileName='config.xml'):
        self._fileName = fileName
        self._siteConf = {}
        self._news = []
        self._tree = etree.parse(self._fileName)
        self._Config = self._tree.getroot()
        val = validate.RssConfValidate()
        if val.Valid is False:
            raise ConfigurationError('Configuration file is invalid')
        self._loadConf()

    def _loadFmtNews(self):
        """ Load news parameters and check output format """
        with open('format.data') as f:
            self._fmt_news = f.read()
        self.fmt_regex = re.compile('[\%\(site\)s]\s*[\%\(title\)s]')
        self.fmt_regex.match(self._fmt_news)
        if self.fmt_regex is None:
            raise FormatError('Format for news output is invalid')

    def _loadConf(self):
        """Configuration loading method"""
        self._loadFmtNews()
        self._siteConf = {child.find('name').text : child.find('url').text
                                           for child in self._Config}

    def loadNewsRss(self, site):
        """Load the news. You have to specify the site."""
        if site in self._siteConf:
            self.feed = feedparser.parse(self._siteConf[site],
                                         agent='RssRead/0.3.3 +https://lucafrancesca.me/')
            self._news = [self._fmt_news %
                          {"site": news.link.encode('utf-8'),
                           "title": news.title.encode('utf-8').decode("utf-8", "ignore")}
                          for news in self.feed.entries]
        else:
            raise SiteError('Site not present')

    @property
    def News(self):
        return self._news
    
    def _addSite(self, name, url, time=str(time.time())):
        """Configuration site adding method. The args are (name, url) """
        if name in self._siteConf:
            raise SiteError('Site already present')
        else:
            Site = etree.SubElement(self._Config, 'site')
            etree.SubElement(Site, 'name').text = name
            etree.SubElement(Site, 'url').text = url
            etree.SubElement(Site, 'lastupdate').text = time
            self._tree.write(self._fileName, encoding='utf-8',
                             xml_declaration=True)
            self._siteConf[name] = url

    def _removeSite(self, site):
        """Configuration site removing method. Just give it the site name """
        if site in self._siteConf:
            for Site in self._Config.findall('site'):
                if Site.find('name').text == site:
                    self._Config.remove(Site)
            self._tree.write(self._fileName, encoding='utf-8',
                             xml_declaration=True)
            del self._siteConf[site]
        else:
            raise SiteError('Site already removed')
            
    def _safe_load(self, site):
        try:
            self.loadNewsRss(site)
        except SiteError:
            print('Site not present!')
        except (FormatError, KeyError, NameError):
            print('Format invalid')
            
    def load(self, site):
        self._safe_load(site)

    def _safe_add(self, site, url):
        try:
            self._addSite(site, url)
        except (NameError, SiteError):
            pass #Already present
        except TypeError:
            print('Url missing')
            
    def addSite(self, site, url):
            self._safe_add(site, url)
    
    def _safe_remove(self, site):
        try:
            self._removeSite(site)
        except (SiteError):
            pass # Not present'
        except (TypeError, NameError):
            pass
        
    def removeSite(self, site):
            self._safe_remove(site)

    def __str__(self):
        data=[]
        data_id = 0
        for news in self.feed.entries:
            item = {data_id: [news.title, news.link]}
            data.append(item)
            data_id += 1
        return json.dumps(data) 
