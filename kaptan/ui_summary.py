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
        self.labelSummary = QLabel()
        groupLayout.addWidget(    self.labelSummary)
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

        if mouseWidget.mouseButtonMap == "RightHanded":
            mouseWidget.mouseButtonMap = self.tr("Right Handed")
        else:
            mouseWidget.mouseButtonMap = self.tr("Left Handed")

        if mouseWidget.folderSingleClick:
            mouseWidget.folderSingleClick = self.tr("Single Click")
        else:
            mouseWidget.folderSingleClick = self.tr("Double Click")

        if themeWidget.desktopType == "org.kde.desktopcontainment":
            themeWidget.desktopType = self.tr("Desktop View")
        else:
            themeWidget.desktopType = self.tr("Folder View")

        if menuWidget.menuSelected == 0:
            menuWidget.menuSelected = self.tr("Application Launcher")
        elif menuWidget.menuSelected == 1:
            menuWidget.menuSelected = self.tr("Application Menu")
        else:
            menuWidget.menuSelected = self.tr("Application Panel")

        if wallpaperWidget.selectWallpaper:
            wallpaperWidget.selectWallpaper = "<img src='{}' width='128' height='96'/>".format(wallpaperWidget.selectWallpaper)

        if avatarWidget.userAvatar:
            avatarWidget.userAvatar = "<img src='{}' width='128' height='128'/>".format(avatarWidget.userAvatar)


        self.summary["Mouse"] = [{"mouseButtonMap" : mouseWidget.mouseButtonMap,
                                  "folderSingleClick" : mouseWidget.folderSingleClick}]


        self.summary["Theme"] = [{"desktopCount" : themeWidget.desktopCount,
                                  "desktopType" : themeWidget.desktopType,
                                  "iconSet" : themeWidget.iconSet.capitalize(),
                                  "themeSet" : themeWidget.themeSet or self.tr("Unspecified.")}]

        self.summary["Menu"] = {"menuSelected" : menuWidget.menuSelected}

        self.summary["Wallpaper"] = {"selectWallpaper" : wallpaperWidget.selectWallpaper or self.tr("Unspecified.")}

        self.summary["Avatar"] = {"userAvatar" : avatarWidget.userAvatar or self.tr("Unspecified.")}


        html = self.tr("""
        <ul>
            <li><strong>Mouse Options</strong>
            </li>
                <ul>
                    <li>Selected Hand: <strong>{}</strong></li>
                    <li>Selected Clicking Behavior: <strong>{}</strong></li>
                </ul>
            <li><strong>Theme Options</strong>
                <ul>
                    <li>Desktop Count: <strong>{}</strong></li>
                    <li>Desktop Type: <strong>{}</strong></li>
                    <li>Icon Set: <strong>{}</strong></li>
                    <li>Theme Set: <strong>{}</strong></li>
                </ul>
            </li>
            <li><strong>Menu Option</strong>
                <ul>
                    <li>Selected Menu: <strong>{}</strong></li>
                </ul>
            </li>
            <li><strong>Selected Wallpaper</strong>
                <ul>
                    <li><strong>{}</strong></li>
                </ul>
            </li>
            <li><strong>Selected Avatar</strong>
                <ul>
                    <li><strong>{}</strong></li>
                </ul>
            </li>
        </ul>""")

        self.labelSummary.setText(html.format(self.summary["Mouse"][0]["mouseButtonMap"], self.summary["Mouse"][0]["folderSingleClick"],
                          self.summary["Theme"][0]["desktopCount"], self.summary["Theme"][0]["desktopType"],
                          self.summary["Theme"][0]["iconSet"], self.summary["Theme"][0]["themeSet"],
                          self.summary["Menu"]["menuSelected"], self.summary["Wallpaper"]["selectWallpaper"],
                          self.summary["Avatar"]["userAvatar"]))