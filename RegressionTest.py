#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RssRead as feed
import unittest


class RegressionTest(unittest.TestCase):

    def setUp(self):
        self.rss = feed.RssRead()

    def test1f(self):
        self.assertNotEqual(self.rss._siteConf, {})

    def test2(self):
        self.rss.loadNewsRss('hwupgrade')
        self.assertNotEqual(self.rss.News, [])

if __name__ == '__main__':
    unittest.main()
