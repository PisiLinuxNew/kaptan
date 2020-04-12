# Copyright 2016 Metehan Özbek <mthnzbk@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.

from PyQt5.QtWidgets import QWizardPage, QLabel, QGroupBox, QListWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QHBoxLayout,\
    QCheckBox, QPushButton, QFileDialog, QListView, QListWidgetItem
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from os.path import join, dirname, abspath
import os
from .tools import Parser

class WallpaperWidget(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSubTitle(self.tr("<h2>Choose Wallpaper</h2>"))

        vlayout = QVBoxLayout(self)

        labelLayout = QHBoxLayout()
        labelImage = QLabel()
        labelImage.setMaximumSize(64,64)
        labelImage.setPixmap(QIcon.fromTheme("preferences-desktop-wallpaper").pixmap(64, 64))
        labelLayout.addWidget(labelImage)

        label = QLabel(self)
        label.setText(self.tr("<p>Choose your favorite wallpaper for Pisi Linux. Don't forget to check out "
                              "<strong>Desktop Settings</strong> for downloading new and cool wallpapers.</p>"))
        label.setWordWrap(True)
        labelLayout.addWidget(label)
        vlayout.addLayout(labelLayout)

        vlayout.addItem(QSpacerItem(20, 40, QSizePolicy.Preferred, QSizePolicy.Preferred))

        groupBox = QGroupBox(self)
        groupBox.setTitle(self.tr("Wallpapers"))
        groupBox.setMinimumHeight(325)

        grLayout = QVBoxLayout(groupBox)
        self.listWidget = QListWidget()
        self.listWidget.setViewMode(QListView.IconMode)
        self.listWidget.setIconSize(QSize(250, 150))
        grLayout.addWidget(self.listWidget)
        vlayout.addWidget(groupBox)

        vlayout.addItem(QSpacerItem(20, 60, QSizePolicy.Preferred, QSizePolicy.Preferred))

        hlayout = QHBoxLayout()
        self.button = QPushButton()
        self.button.setText(self.tr("Choose Wallpaper from File"))
        hlayout.addWidget(self.button)

        hlayout.addItem(QSpacerItem(400, 20, QSizePolicy.Preferred, QSizePolicy.Preferred))

        self.checkbox = QCheckBox()
        self.checkbox.setText(self.tr("Don't Change Wallpaper"))
        hlayout.addWidget(self.checkbox)

        vlayout.addLayout(hlayout)

        self.checkbox.clicked.connect(self.wallpaperChecked)
        self.button.clicked.connect(self.wallpaperSelectDialog)
        self.listWidget.itemClicked.connect(self.wallpaperSelect)

        self.selectWallpaper = None
        self.wallpapersParser()

    def wallpapersParser(self):
        wallpaperPath = "/usr/share/wallpapers"
        for folder in os.listdir(wallpaperPath):
            path = join(wallpaperPath,folder, "contents")
            thumbFolder = os.listdir(path)
            for thumb in thumbFolder:
                if thumb.startswith("scre"):
                    item = QListWidgetItem(self.listWidget)

                    pix = QPixmap(join(path, thumb))
                    pix = pix.scaled(QSize(240, 140), Qt.IgnoreAspectRatio, Qt.FastTransformation)

                    item.setIcon(QIcon(pix))
                    item.setSizeHint(QSize(250, 150))
                    item.screenshotPath = join(path, thumb)

    def wallpaperSelect(self, item):
        if hasattr(item, "userSelect"):
            self.selectWallpaper = item.screenshotPath
        else:
            path = join(dirname(abspath(item.screenshotPath)), "images")
            list = os.listdir(path)
            list.sort()
            self.selectWallpaper = join(path, list[-1])

    def wallpaperChecked(self):
        if self.checkbox.isChecked():
            self.selectWallpaper = None
            self.listWidget.setDisabled(True)
            self.button.setDisabled(True)
        else:
            self.listWidget.clearSelection()
            self.listWidget.setEnabled(True)
            self.button.setEnabled(True)

    def wallpaperSelectDialog(self):
        file_url, file_type = QFileDialog.getOpenFileName(self, self.tr("Choose Wallpaper"), QDir.homePath(), "Image (*.png *.jpg)")
        print(file_url)
        if not "" == file_url:
            self.selectWallpaper = file_url
            item = QListWidgetItem(self.listWidget)
            item.setIcon(QIcon(file_url))
            item.screenshotPath = file_url
            item.userSelect = True
            self.listWidget.setCurrentItem(item)

    def execute(self):
        if self.selectWallpaper is None:
            pass
        else:
            configFilePath = join(QDir.homePath(), ".config", "plasma-org.kde.plasma.desktop-appletsrc")
            parser = Parser(configFilePath)
            wallpaper = parser.getWallpaper()
            if wallpaper is not None:
                parser.setWallpaper(self.selectWallpaper)
            else:
                entireWallpaperConfigString = "\n[Containments][52][Wallpaper][org.kde.image][" \
                                              "General]\nFillMode=0\nImage=file://{!s}\n".format(self.selectWallpaper)
                with open(configFilePath, "a") as fp:
                    fp.write(entireWallpaperConfigString)

