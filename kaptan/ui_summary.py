from PyQt5.QtWidgets import QWizardPage, QLabel, QGroupBox, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class SummaryWidget(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSubTitle(self.tr("<h2>Ayarlarınızı Kaydedin</h2>"))

        vlayout = QVBoxLayout(self)

        label = QLabel(self)
        label.setWordWrap(True)
        label.setText(self.tr("<p>Bütün adımları başarıyla tamamladınız. Aşağıda uygulanmasını istediğiniz ayarların listesini \
        görebilirsiniz. <strong>Ayarları Uygula</strong> tuşuna bastığınızda ayarlarınız kaydedilecektir. Artık Pisi Linux'un \
        tadınız çıkarmaya hazırsınız!</p>"))
        vlayout.addWidget(label)
        vlayout.addItem(QSpacerItem(20, 40, QSizePolicy.Preferred, QSizePolicy.Preferred))

        groupBox = QGroupBox()
        groupBox.setTitle(self.tr("Aşağıdaki Ayarlar Uygulanacaktır"))
        groupBox.setMinimumHeight(350)

        groupLayout = QVBoxLayout(groupBox)
        summaryLabel = QLabel()
        groupLayout.addWidget(summaryLabel)
        vlayout.addWidget(groupBox)

        vlayout.addItem(QSpacerItem(20, 40, QSizePolicy.Preferred, QSizePolicy.Preferred))