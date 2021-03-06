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
# by Luca Francesca, 2017

from __future__ import absolute_import
from __future__ import print_function
import RssConfValidate as validate


tst = validate.RssConfValidate()

if tst.Valid is True:
    print("Valid configuration")
else:
    print("Invalid configuration")

