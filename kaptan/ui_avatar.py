from PyQt5.QtWidgets import QWizardPage, QLabel, QGroupBox, QVBoxLayout, QSpacerItem, QSizePolicy, QHBoxLayout,\
    QComboBox, QPushButton
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class AvatarWidget(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle("<h2>Kullanıcı Resminizi Yaratın</h2>")
        self.setSubTitle(" ")

        vlayout = QVBoxLayout(self)
        label = QLabel(self)
        label.setWordWrap(True)
        label.setText("<p>Bu ekran <strong>kullanıcı resminizi</strong> seçmenize yardımcı olur. Dosyalarınız arasından bir resim seçebilir \
        ya da kameradan aldığınız görüntüyü kullanabilirsiniz. <strong>Seçenekler</strong> menüsünden seçiminizi yapabilirsiniz.</p>")
        vlayout.addWidget(label)

        vlayout.addItem(QSpacerItem(20, 40, QSizePolicy.Preferred, QSizePolicy.Preferred))

        groupBox = QGroupBox()
        vlayout2 = QVBoxLayout(groupBox)
        hlayout = QHBoxLayout()
        comboBox = QComboBox()
        buttonCam = QPushButton()
        buttonReplay = QPushButton()

        hlayout.addWidget(comboBox)
        hlayout.addWidget(buttonCam)
        hlayout.addWidget(buttonReplay)

        vlayout2.addLayout(hlayout)

        label2 = QLabel()
        label2.setText("qweq")
        label2.setMinimumSize(300, 300)

        vlayout2.addWidget(label2)

        vlayout.addWidget(groupBox)
        vlayout.addItem(QSpacerItem(20, 40, QSizePolicy.Preferred, QSizePolicy.Preferred))