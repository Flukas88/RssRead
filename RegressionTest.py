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
        self.rss.loadNewsRss('slashdot')
        self.assertNotEqual(self.rss.News, [], 'Problems with rss loading')


if __name__ == '__main__':
    unittest.main()
