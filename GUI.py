#!/usr/bin/env python
#-*- coding:utf-8 -*-

from PyQt4 import QtGui, QtCore
import wallpaper_download
import sys
from math import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.folderName =os.path.dirname(sys.argv[0])
        self.lineedit = QLineEdit(self.folderName)
        self.pushButtonOpen = QtGui.QPushButton(self)
        self.pushButtonOpen.setText("Open Folder")
        self.pushButtonSave= QtGui.QPushButton(self)
        self.pushButtonSave.setText("&Save")
        self.layoutHorizontal = QtGui.QHBoxLayout(self)
        self.layoutHorizontal.addWidget(self.pushButtonOpen)
        self.layoutHorizontal.addWidget(self.lineedit)
        self.layoutHorizontal.addWidget(self.pushButtonSave)
        self.setWindowTitle("GetBingWallPaper")

        self.pushButtonOpen.clicked.connect(self.on_pushButtonOpen_clicked)
        self.pushButtonSave.clicked.connect(wallpaper_download.picurl)

    @QtCore.pyqtSlot()
    def on_pushButtonOpen_clicked(self):
        self.folderName = QtGui.QFileDialog.getExistingDirectory(
            self, "Open Directory",
            "/path/to/folder",
            QtGui.QFileDialog.ShowDirsOnly | QtGui.QFileDialog.DontResolveSymlinks,
        )
        wallpaper_download.path=self.folderName
        print self.folderName
        self.lineedit.setText(self.folderName)


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('MyWindow')

    main = MyWindow()
    main.show()

    sys.exit(app.exec_())