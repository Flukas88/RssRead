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
# by Luca Francesca, 2014

import RssConfValidate as validate
import unittest


class RegressionTest(unittest.TestCase):

    def setUp(self):
        self.tst = validate.RssConfValidate('config_fake.xml')

    def test_configuration_content_wrong(self):
        self.assertTrue(self.tst.Valid, 'Expected failure on wrong config file.')

    def test_configuration_content_right(self):
        self.tst = validate.RssConfValidate('config_right.xml')
        self.assertTrue(self.tst.Valid, 'Right file ok.')

if __name__ == '__main__':
    unittest.main()
