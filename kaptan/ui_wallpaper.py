from PyQt5.QtWidgets import QWizardPage, QLabel, QGroupBox, QListWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QHBoxLayout,\
    QCheckBox, QPushButton, QFileDialog
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class WallpaperWidget(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSubTitle(self.tr("<h2>Duvar Kağıdı Seçin</h2>"))

        vlayout = QVBoxLayout(self)

        label = QLabel(self)
        label.setText(self.tr("<p>Masaüstünüz için en beğendiğiniz duvar kağıdını seçin. <strong>Masaüstü Ayarları</strong>'na \
        girerek yeni ve havalı duvar kağıtları indirebileeğinizi unutmayın.</p>"))
        label.setWordWrap(True)
        vlayout.addWidget(label)

        vlayout.addItem(QSpacerItem(20, 40, QSizePolicy.Preferred, QSizePolicy.Preferred))

        groupBox = QGroupBox(self)
        groupBox.setTitle(self.tr("Duvar Kağıtları"))
        groupBox.setMinimumHeight(350)

        grLayout = QVBoxLayout(groupBox)
        self.listWidget = QListWidget()
        grLayout.addWidget(self.listWidget)
        vlayout.addWidget(groupBox)

        vlayout.addItem(QSpacerItem(20, 40, QSizePolicy.Preferred, QSizePolicy.Preferred))

        hlayout = QHBoxLayout()
        self.button = QPushButton()
        self.button.setText(self.tr("Kendi Duvar Kağıdını Seç"))
        hlayout.addWidget(self.button)

        hlayout.addItem(QSpacerItem(400, 20, QSizePolicy.Preferred, QSizePolicy.Preferred))

        self.checkbox = QCheckBox()
        self.checkbox.setText(self.tr("Duvar Kağıdını değiştirme"))
        hlayout.addWidget(self.checkbox)

        vlayout.addLayout(hlayout)

        self.checkbox.clicked.connect(self.wallpaperChecked)
        self.button.clicked.connect(self.wallpaperSelect)

    def wallpaperChecked(self):
        if self.checkbox.isChecked():
            self.listWidget.setDisabled(True)
            self.button.setDisabled(True)
        else:
            self.listWidget.setEnabled(True)
            self.button.setEnabled(True)

    def wallpaperSelect(self):
        file_url, file_type = QFileDialog.getOpenFileName(self, self.tr("Duvar Kağıdını Seç"), QDir.homePath(), "Image (*.png *.jpg)")
        print(file_url)
        if not "" == file_url:
            pass

    def execute(self): pass