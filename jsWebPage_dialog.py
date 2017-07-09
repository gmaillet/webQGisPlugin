# -*- coding: utf-8 -*-
"""
/***************************************************************************
 jsWebPageDialog
                                 A QGIS plugin jsWebPage
                             -------------------
        begin                : 2017-07-09
        git sha              : $Format:%H$
        copyright            : (C) 2017 by Greg
        email                : gregoire.maillet@gmail.com
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

import os

from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtWebKit import QWebView
from PyQt4.QtWebKit import QWebPage
from PyQt4.QtCore import QUrl
from qgis.core import *
from qgis.gui import *
from qgis.utils import *

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'jsWebPage_dialog_base.ui'))

class WebPage(QWebPage):
	def __init__(self,console):
		super(WebPage,self).__init__()
		self.console = console

	def javaScriptConsoleMessage(self, msg, lineNumber, sourceID):
		self.console.append("JsConsole(%s:%d): %s" % (sourceID, lineNumber, msg))

class jsWebPageDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(jsWebPageDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
	webPage = WebPage(self.consoleTextEdit)
	self.webView.setPage(webPage)
	self.urlLineEdit.editingFinished.connect(self.onUrlReady)
	self.jsLineEdit.editingFinished.connect(self.onJsReady)
	self.sendPositionButton.clicked.connect(self.onSendPosition)

    def setPosition(self,strPosition):
	self.consoleTextEdit.append('setPosition(\''+strPosition+'\')')
	self.webView.page().mainFrame().evaluateJavaScript('setPosition(\''+strPosition+'\')')

    def onSendPosition(self):
	self.setPosition(str(iface.mapCanvas().center())+' in '+iface.mapCanvas().mapRenderer().destinationCrs().authid())
	#self.consoleTextEdit.append("position : "+str(iface.mapCanvas().center())+' in '+iface.mapCanvas().mapRenderer().destinationCrs().authid())	
    def onJsReady(self):
	self.webView.page().mainFrame().evaluateJavaScript(self.jsLineEdit.text())
	
    def onUrlReady(self):
        self.consoleTextEdit.setText(self.urlLineEdit.text())
        self.webView.load(QUrl(self.urlLineEdit.text()))
