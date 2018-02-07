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
import RssRead as feed
import unittest
import time 
import string

class RegressionTest(unittest.TestCase):

    def setUp(self):
        self.rss = feed.RssRead()

    def test_configuration_loading(self):
        self.assertNotEqual(self.rss._siteConf, {}, 'Problems with configuration loading')

    def test_fmt_loading_sintax(self):
        try:
            self.rss.loadNewsRss('slashdot')
        except feed.FormatError:
            self.fail('Format for news output is invalid')

    def test_loading_news(self):
        try:
            self.rss.loadNewsRss('slashdot')
        except KeyError:
            self.fail('Error loading news, unexpected')

    def test_unicode_except(self):
        try:
            self.rss.loadNewsRss('python')
        except (UnicodeEncodeError, KeyError):
            self.fail('Unicode Error thrown, unexpected')

    def test_add_site_twice(self):
        self.rss.addSite('NAME', 'URL')
        try:
            self.rss.addSite('NAME', 'URL')
        except (TypeError, feed.SiteError):
            self.fail('Already present site exception thrown, expected')

    def test_remove_site_twice(self):
        self.rss.removeSite('NAME')
        try:
            self.rss.removeSite('NAME')
        except (TypeError, feed.SiteError):
            self.fail('Already removed site exception thrown, expected')

    def test_already_present_site(self):
        try:
            self.rss.loadNewsRss('python')
        except (TypeError, feed.SiteError):
            self.fail('Site already present exception thrown, expected')

    def test_site_not_present(self):
        try:
            self.rss.loadNewsRss('asdasd')
        except (TypeError, feed.SiteError):
            pass 

if __name__ == '__main__':
    unittest.main()
