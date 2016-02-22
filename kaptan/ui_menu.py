from PyQt5.QtWidgets import QWizardPage, QLabel, QVBoxLayout, QSpacerItem, QSizePolicy, QHBoxLayout, QComboBox
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from os.path import join
from kaptan.tools import *


class MenuWidget(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSubTitle(self.tr("<h2>Bir Menü Stili Seçin</h2>"))

        texts = [
            self.tr("<p>Kickoff Menü, Pisi Linux'un ön tanımlı menüsüdür.</p>\
            <p>Uygulama kısayolları hızlı ve kolay erişebilecek şekilde düzenlenmiştir.</p>"),
            self.tr("<p>Basit menü KDE 3'ten kalma eski bir menü stilidir.</p>\
            <p>Oldukça hafif yapısı yüzünden yavaş bilgisayarlar için önerilir.</p>"),
            self.tr("<p>Lancelot menü, geniş ve oldukça kişiselleştirilebilir bir menüdür.</p>\
            <p>Uygulama kısayolları hızlı ve kolay erişilebilecek şekilde düzenlenmiştir.</p>")
        ]

        self.menus = [[":/data/images/menu-kickoff.png", texts[0]],
                 [":/data/images/menu-kicker.png", texts[1]],
                 [":/data/images/menu-kimpanel.png", texts[2]]]

        vlayout = QVBoxLayout(self)

        labelLayout = QHBoxLayout()

        iconLabel = QLabel()
        iconLabel.setMaximumSize(64, 64)
        iconLabel.setPixmap(QPixmap(":/data/images/kde.png"))
        labelLayout.addWidget(iconLabel)

        label = QLabel(self)
        label.setText(self.tr("KDE menüsünü istediğiniz stili seçerek kişiselleştirebilirsiniz.!"))
        labelLayout.addWidget(label)
        vlayout.addLayout(labelLayout)

        vlayout.addItem(QSpacerItem(20, 40, QSizePolicy.Preferred, QSizePolicy.Preferred))

        self.comboBox = QComboBox(self)
        self.comboBox.addItem(self.tr("Kickoff Menü"))
        self.comboBox.addItem(self.tr("Kicker Menü"))
        self.comboBox.addItem(self.tr("KimPanel Menü"))
        vlayout.addWidget(self.comboBox)

        vlayout.addItem(QSpacerItem(20, 40, QSizePolicy.Preferred, QSizePolicy.Preferred))

        hlayout = QHBoxLayout(self)

        self.labelMenu = QLabel(self)
        self.labelMenu.setPixmap(QPixmap(self.menus[0][0]))
        self.labelMenu.setMaximumSize(350 ,214)
        hlayout.addWidget(self.labelMenu)
        self.labelText = QLabel(self)
        self.labelText.setWordWrap(True)
        self.labelText.setText(self.tr(self.menus[0][1]))
        hlayout.addWidget(self.labelText)

        vlayout.addLayout(hlayout)

        vlayout.addItem(QSpacerItem(20, 40, QSizePolicy.Preferred, QSizePolicy.Preferred))

        self.comboBox.currentIndexChanged.connect(self.menuSelect)

        self.menuSelected = 0


    def menuSelect(self, index):
        self.menuSelected = index
        self.labelMenu.setPixmap(QPixmap(self.menus[index][0]))
        self.labelText.setText(self.menus[index][1])

    def execute(self):
        menus = ["org.kde.plasma.kickoff", "org.kde.plasma.kicker", "org.kde.plasma.kimpanel"]
        menu = menus[self.menuSelected]

        configFilePath = join(QDir.homePath(), ".config5", "plasma-org.kde.plasma.desktop-appletsrc")
        configFile = open(configFilePath).read()
        menuStyle = getMenuStyle(configFile)

        if menu != menuStyle[1]:
            with open(configFilePath, "w") as newConfigFile:
                newConfigFile.write(setMenuStyle(configFile))
                newConfigFile.close()



        settings1 = QSettings(join(QDir.homePath(), ".config5", "plasma-org.kde.plasma.desktop-appletsrc"), QSettings.IniFormat)
        #settings1.setValue("", 2)
        #settings1.setValue("", 2)
        settings1.sync()