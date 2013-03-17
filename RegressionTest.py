#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RssRead as feed
import unittest


class RegressionTest(unittest.TestCase):

    def setUp(self):
        self.rss = feed.RssRead()

    def test_configuration(self):
        self.assertNotEqual(self.rss._siteConf, {}, 'Problems with configuration loading')

    def test_loading(self):
        self.rss.loadNewsRss('torrent')
        self.assertNotEqual(self.rss.News, [], 'Problems with rss loading')

    def test_unicode_except(self):
        try:
            self.rss.loadNewsRss('torrent')
        except UnicodeEncodeError:
            self.fail('Unicode Error thrown')

    def test_add_site(self):
        try:
            self.rss.loadNewsRss('torrent')
            self.rss += 'io', 'tu'
        except TypeError:
            self.fail('Already present site exception thrown')

    def test_remove_site(self):
        try:
            self.rss.loadNewsRss('torrent')
            self.rss -= 'io'
        except TypeError:
            self.fail('Already removed site exception thrown')


if __name__ == '__main__':
    unittest.main()
