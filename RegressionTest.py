#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RssRead as feed
import unittest


class RegressionTest(unittest.TestCase):

    def setUp(self):
        self.rss = feed.RssRead()

    def test1f(self):
        self.assertNotEqual(self.rss._siteConf, {}, 'Problems with configuration loading')

    def test2(self):
        self.rss.loadNewsRss('slashdot')
        self.assertNotEqual(self.rss.News, [], 'Problems with rss loading')

if __name__ == '__main__':
    unittest.main()
