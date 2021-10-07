# -*- coding: utf-8 -*-

"""
/***************************************************************************
 Deg2dms
                                 A QGIS plugin
 This plugin converts deg to DMS in table
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2021-10-04
        copyright            : (C) 2021 by Ivan Lebedev
        email                : lebedev77@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Ivan Lebedev'
__date__ = '2021-10-04'
__copyright__ = '(C) 2021 by Ivan Lebedev'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'


def dms2deg(dms):
    dmss = dms.split()
    return float(dmss[0]) + float(dmss[1]) / 60 + float(dmss[2]) / 3600


def deg2dms(deg):
    d = int(deg)
    m = int((deg - d) * 60)
    s = float(((deg - d) * 60 - m) * 60)
    return '{} {} {}'.format(d, m, round(s, 2))
