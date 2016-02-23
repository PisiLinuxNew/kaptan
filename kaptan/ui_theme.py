from PyQt5.QtWidgets import QWizardPage, QLabel, QGroupBox, QListWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QHBoxLayout,\
    QSpinBox, QComboBox, QListView, QListWidgetItem
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import *
from os.path import join
from kaptan.tools import getDesktopStyle, setDesktopStyle

class ThemeWidget(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSubTitle(self.tr("<h2>Customize Your Desktop</h2>"))

        vlayout = QVBoxLayout(self)

        labelLayout = QHBoxLayout()
        imageLabel = QLabel()
        imageLabel.setMaximumSize(64, 64)
        imageLabel.setPixmap(QPixmap(":/data/images/preferences-desktop-color.png"))
        labelLayout.addWidget(imageLabel)

        label = QLabel(self)
        label.setText(self.tr("<p>Choose your favorite theme and desktop type. Customize Pisi Linux with colorful styles and themes.</p>"))
        labelLayout.addWidget(label)
        vlayout.addLayout(labelLayout)

        vlayout.addItem(QSpacerItem(20, 40, QSizePolicy.Preferred, QSizePolicy.Preferred))
        self.createGroupBox(vlayout)
        self.createDesktopOption(vlayout)

        self.desktopCount = 1
        self.desktopType = "org.kde.desktopcontainment"
        self.iconSet = "breeze"
        self.themeSet = None

    def createGroupBox(self, layout):

        group1 = QGroupBox(self)
        group1.setTitle(self.tr("KDE Themes"))
        group1.setMinimumHeight(180)
        layout.addWidget(group1)

        grLayout = QVBoxLayout(group1)
        listWidget1 = QListWidget(group1)
        grLayout.addWidget(listWidget1)

        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Preferred, QSizePolicy.Preferred))


        group2 = QGroupBox(self)
        group2.setTitle(self.tr("İcon Sets"))
        group2.setMinimumHeight(140)
        group2.setMaximumHeight(150)
        layout.addWidget(group2)

        grLayout2 = QVBoxLayout(group2)
        listWidget2 = QListWidget(group2)
        listWidget2.setViewMode(QListView.IconMode)
        listWidget2.setIconSize(QSize(384, 72))
        item = QListWidgetItem(listWidget2)
        item.setIcon(QIcon(":/data/images/oxygen-set.png"))
        item.setText("Oxygen")

        item = QListWidgetItem(listWidget2)
        item.setIcon(QIcon(":/data/images/breeze-set.png"))
        item.setText("Breeze")
        item.setSelected(True)

        listWidget2.itemClicked.connect(self.iconSetSelect)

        grLayout2.addWidget(listWidget2)

    def iconSetSelect(self, item):
        self.iconSet = str(item.text()).lower()

    def createDesktopOption(self, layout):
        hlayout = QHBoxLayout()
        layout.addLayout(hlayout)

        vlayout1 = QVBoxLayout()
        vlayout2 = QVBoxLayout()
        hlayout.addLayout(vlayout1)
        hlayout.addLayout(vlayout2)

        label1 = QLabel()
        label1.setText(self.tr("Desktop Type"))
        vlayout1.addWidget(label1)
        label2 = QLabel()
        label2.setText(self.tr("Number of Desktops"))
        vlayout2.addWidget(label2)

        comboBox = QComboBox()
        comboBox.addItem(self.tr("Desktop View"))
        comboBox.addItem(self.tr("Folder View"))
        comboBox.currentIndexChanged.connect(self.desktopTypeCreate)
        vlayout1.addWidget(comboBox)
        spinBox = QSpinBox()
        spinBox.setMinimum(1)
        spinBox.setMaximum(20)
        spinBox.valueChanged.connect(self.desktopCreate)
        vlayout2.addWidget(spinBox)

    def desktopCreate(self, value):
        self.desktopCount = value

    def desktopTypeCreate(self, value):
        if value == 0:
            self.desktopType = "org.kde.desktopcontainment"
        else:
            self.desktopType = "org.kde.folder"

    def execute(self):
        settings1 = QSettings(join(QDir.homePath(), ".config5", "kwinrc"), QSettings.IniFormat)
        settings1.setValue("Desktops/Number", self.desktopCount)
        settings1.setValue("Desktops/Rows", 2)
        settings1.sync()


        settings3 = QSettings(join(QDir.homePath(), ".config5", "kdeglobals"), QSettings.IniFormat)
        settings3.setValue("Icons/Theme", self.iconSet)
        settings3.sync()

        configFilePath = join(QDir.homePath(), ".config5", "plasma-org.kde.plasma.desktop-appletsrc")

        configFile = open(configFilePath).read()
        desktopView = getDesktopStyle(configFile)

        if self.desktopType != desktopView[1]:
            with open(configFilePath, "w") as newConfigFile:
                newConfigFile.write(setDesktopStyle(configFile))
                newConfigFile.close()