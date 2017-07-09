# -*- coding: utf-8 -*-
"""
/***************************************************************************
 jsWebPage
                                 A QGIS plugin
 create a webPage plugin (for 3D view based on iTowns)
                             -------------------
        begin                : 2017-07-09
        copyright            : (C) 2017 by gmaillet
        email                : gregoire.maillet@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load jsWebPage class from file jsWebPage.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .jsWebPage import jsWebPage
    return jsWebPage(iface)
