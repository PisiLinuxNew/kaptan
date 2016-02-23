from PyQt5.QtWidgets import QWizardPage, QLabel, QGroupBox, QListWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QHBoxLayout,\
    QCheckBox, QPushButton, QFileDialog, QListView, QDesktopWidget, QListWidgetItem
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from os.path import join, dirname, abspath
import os

class WallpaperWidget(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSubTitle(self.tr("<h2>Choose Wallpaper</h2>"))

        vlayout = QVBoxLayout(self)

        labelLayout = QHBoxLayout()
        labelImage = QLabel()
        labelImage.setMaximumSize(64,64)
        labelImage.setPixmap(QPixmap(":/data/images/preferences-desktop-wallpaper.png"))
        labelLayout.addWidget(labelImage)

        label = QLabel(self)
        label.setText(self.tr("<p>Choose your favorite wallpaper for Pisi Linux. Don't forget to check out \
        <strong>Desktop Settings</strong> for downloading new and cool wallpapers.</p>"))
        label.setWordWrap(True)
        labelLayout.addWidget(label)
        vlayout.addLayout(labelLayout)

        vlayout.addItem(QSpacerItem(20, 40, QSizePolicy.Preferred, QSizePolicy.Preferred))

        groupBox = QGroupBox(self)
        groupBox.setTitle(self.tr("Wallpapers"))
        groupBox.setMinimumHeight(350)

        grLayout = QVBoxLayout(groupBox)
        self.listWidget = QListWidget()
        self.listWidget.setViewMode(QListView.IconMode)
        self.listWidget.setIconSize(QSize(250, 150))
        grLayout.addWidget(self.listWidget)
        vlayout.addWidget(groupBox)

        vlayout.addItem(QSpacerItem(20, 40, QSizePolicy.Preferred, QSizePolicy.Preferred))

        hlayout = QHBoxLayout()
        self.button = QPushButton()
        self.button.setText(self.tr("Choose wallpaper from file"))
        hlayout.addWidget(self.button)

        hlayout.addItem(QSpacerItem(400, 20, QSizePolicy.Preferred, QSizePolicy.Preferred))

        self.checkbox = QCheckBox()
        self.checkbox.setText(self.tr("Don't change wallpaper"))
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
                    item.setIcon(QIcon(join(path, thumb)))
                    item.screenshotPath = join(path, thumb)

    def wallpaperSelect(self, item):
        if hasattr(item, "userSelect"):
            self.selectWallpaper = item.screenshotPath
        else:
            path = join(dirname(abspath(item.screenshotPath)), "images")
            list = os.listdir(path)
            list.sort()
            self.selectWallpaper = join(path, list[-1])
            r = QDesktopWidget().screenGeometry()
            print(r.width())

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
        file_url, file_type = QFileDialog.getOpenFileName(self, self.tr("Choose wallpaper"), QDir.homePath(), "Image (*.png *.jpg)")
        print(file_url)
        if not "" == file_url:
            self.selectWallpaper = file_url
            item = QListWidgetItem(self.listWidget)
            item.setIcon(QIcon(file_url))
            item.screenshotPath = file_url
            item.userSelect = True
            self.listWidget.setCurrentItem(item)

    def execute(self):
        screenRect = QDesktopWidget.screenGeometry()
        width = screenRect.width()
        height =screenRect.height()

        settings = QSettings(join(QDir.homePath(), ".config5", "plasma-org.kde.plasma.desktop-appletsrc"), QSettings.IniFormat)
        settings.setValue("Containments/Image", QUrl(self.selectWallpaper))
        settings.setValue("Containments/width", width)
        settings.setValue("Containments/height", height)
        settings.sync()