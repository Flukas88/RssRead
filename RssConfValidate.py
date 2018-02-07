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
from lxml import etree


class RssConfValidate:
    def __init__(self, fileName='config.xml', fileConfig='config.xsd'):
        self._fileName = fileName
        self._fileConfig = fileConfig
        self._valid = True
        self.schema_f = etree.parse(fileConfig)
        self._validateConf()

    def _validateConf(self):
        schema = etree.XMLSchema(self.schema_f)
        parser = etree.XMLParser(schema = schema)
        with open(self._fileName) as f_source:
            try:
                doc = etree.parse(f_source, parser)
            except etree.XMLSyntaxError:
                self.Valid = False

    @property
    def Valid(self):
        return self._valid

    @Valid.setter
    def Valid(self, value):
        self._valid = value
