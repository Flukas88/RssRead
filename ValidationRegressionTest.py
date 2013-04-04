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
# RssRead 0.3.1
# by Luca Francesca, 2013

import RssConfValidate as validate
import unittest


class RegressionTest(unittest.TestCase):

    def setUp(self):
        self.tst = validate.RssConfValidate()

    def test_configuration_content(self):
        self.assertTrue(self.tst.Valid, 'Problems with validity of config file.')

if __name__ == '__main__':
    unittest.main()