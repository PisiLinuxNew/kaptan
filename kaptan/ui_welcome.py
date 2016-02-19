from PyQt5.QtWidgets import QWizardPage, QLabel, QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

Welcome = """<h1>Pisi Linux Nedir?</h1>
<p><strong>Pisi Linux</strong> güvenilir, hızlı ve kullanıcı dostu bir işletim sistemidir.</p>
<p>Pisi Linux ile internete bağlanabilir, e-postalarınızı okuyabilir, ofis dökümanlarıyla çalışabilir, film izleyebilir,\
 müzik dinleyebilir, yazılım geliştirebilir, oyunlar oynayabilir ve daha fazlasını yapabilirsiniz!</p>
<p><strong>Kaptan</strong>, Pisi Linux çalışma ortamınızı hızlı ve kolayca kişiselleştirmenize yardımcı olan bir uygulamadır. Lütfen \
başlamak için <strong>İleri</strong>'ye tıklayın.</p>
"""

class WelcomeWidget(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSubTitle(self.tr("<h2>Pisi Linux'a Hoş Geldiniz!</h2>"))

        vlayout = QVBoxLayout(self)
        vlayout.addItem(QSpacerItem(20, 150, QSizePolicy.Preferred, QSizePolicy.Minimum))

        hlayout = QHBoxLayout(self)
        label = QLabel(self)
        label.setText(self.tr(Welcome))
        label.setWordWrap(True)
        label.setAlignment(Qt.AlignLeft)
        hlayout.addWidget(label)

        kaptan_logo = QLabel(self)
        kaptan_logo.setPixmap(QPixmap(":/data/images/kaptan_welcome.png"))
        kaptan_logo.setAlignment(Qt.AlignRight)
        kaptan_logo.setMaximumSize(157, 181)
        hlayout.addWidget(kaptan_logo)
        vlayout.addLayout(hlayout)

        vlayout.addItem(QSpacerItem(20, 40, QSizePolicy.Preferred, QSizePolicy.Preferred))