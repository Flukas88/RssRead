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
# RssRead 0.2
# by Luca Francesca, 2013

import RssRead as feed
import unittest


class RegressionTest(unittest.TestCase):

    def setUp(self):
        self.rss = feed.RssRead()

    def test_configuration(self):
        self.assertNotEqual(self.rss._siteConf, {}, 'Problems with configuration loading')

    def test_loading(self):
        self.rss.loadNewsRss('python')
        self.assertNotEqual(self.rss.News, [], 'Problems with rss loading')

    def test_unicode_except(self):
        try:
            self.rss.loadNewsRss('torrent')
        except UnicodeEncodeError:
            self.fail('Unicode Error thrown')

    def test_add_site(self):
        try:
            self.rss += 'io', 'tu'
            self.rss += 'io', 'tu'
        except TypeError:
            self.fail('Already present site exception thrown, expected')

    def test_remove_site(self):
        self.rss -= 'io'
        try:
            self.rss -= 'io'
        except TypeError:
            self.fail('Already removed site exception thrown, expected')

    def test_present_site(self):
        try:
            self.rss.loadNewsRss('hwupgrade.it')
        except feed.SiteError:
            self.fail('Site not present exception thrown, expected')


if __name__ == '__main__':
    unittest.main()
