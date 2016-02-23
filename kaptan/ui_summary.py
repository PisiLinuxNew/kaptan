from PyQt5.QtWidgets import QWizardPage, QLabel, QGroupBox, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class SummaryWidget(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSubTitle(self.tr("<h2>Save Your Settings</h2>"))

        vlayout = QVBoxLayout(self)

        label = QLabel(self)
        label.setWordWrap(True)
        label.setText(self.tr("<p>You have successfully finished all steps. Here's a summary of the settings you want to apply. \
        Click <strong>Apply Settings</strong> to save them now. You are now ready to enjoy Pisi Linux!</p>"))
        vlayout.addWidget(label)
        vlayout.addItem(QSpacerItem(20, 40, QSizePolicy.Preferred, QSizePolicy.Preferred))

        groupBox = QGroupBox()
        groupBox.setTitle(self.tr("The following settings will be applied"))
        groupBox.setMinimumHeight(350)

        groupLayout = QVBoxLayout(groupBox)
        summaryLabel = QLabel()
        groupLayout.addWidget(summaryLabel)
        vlayout.addWidget(groupBox)

        vlayout.addItem(QSpacerItem(20, 40, QSizePolicy.Preferred, QSizePolicy.Preferred))

        self.summary = {}
        self.parent().summaryVisible.connect(self.summaryWrite)

    def summaryWrite(self):
        # -----------QFrame ---QWidget---Kaptan :S
        parent = self.parent().parent().parent()
        #MouseWidget
        mouseWidget = parent.page(1)
        #ThemeWidget
        themeWidget = parent.page(2)
        #MenuWidget
        menuWidget = parent.page(3)
        #WallpaperWidget
        wallpaperWidget = parent.page(4)
        #AvatarWidget
        avatarWidget = parent.page(5)

        self.summary["Mouse"] = [{"mouseButtonMap" : mouseWidget.mouseButtonMap},
                                 {"reverseScrollPolarity" : mouseWidget.reverseScrollPolarity},
                                 {"folderSingleClick" : mouseWidget.folderSingleClick}]

        self.summary["Theme"] = [{"desktopCount" : themeWidget.desktopCount},
                                 {"desktopType" : themeWidget.desktopType},
                                 {"iconSet" : themeWidget.iconSet},
                                 {"themeSet" : themeWidget.themeSet}]

        self.summary["Menu"] = {"menuSelected" : menuWidget.menuSelected}

        self.summary["Wallpaper"] = {"selectWallpaper" : wallpaperWidget.selectWallpaper}

        self.summary["Avatar"] = {"userAvatar" : avatarWidget.userAvatar}