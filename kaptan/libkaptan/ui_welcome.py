# Copyright 2016 Metehan Özbek <mthnzbk@gmail.com>
#           2020 Erdem Ersoy <erdemersoy@erdemersoy.net>
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

from PyQt5.QtWidgets import QWizardPage, QLabel, QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class WelcomeWidget(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSubTitle(self.tr("<h2>Welcome to Pisi Linux!</h2>"))

        vlayout = QVBoxLayout(self)
        vlayout.addItem(QSpacerItem(20, 150, QSizePolicy.Preferred, QSizePolicy.Minimum))

        hlayout = QHBoxLayout(self)
        label = QLabel(self)
        label.setText(self.tr("""<h1>What is Pisi Linux?</h1>
        <p><strong>Pisi Linux</strong> is a reliable, secure, fast and user friendly operating system.</p>
        <p>With Pisi Linux, you can connect to the internet, read your e-mails, work with your office documents,
         watch movies, play music, develop applications, play games and much more!</p>
        <p><strong>Kaptan</strong>, will help you personalize your Pisi Linux workspace easily and quickly.
         Please click <strong>Next</strong> in order to begin.</p>"""))
        label.setWordWrap(True)
        label.setAlignment(Qt.AlignLeft)
        hlayout.addWidget(label)

        kaptan_logo = QLabel(self)
        kaptan_logo.setScaledContents(True)
        kaptan_logo.setPixmap(QPixmap("/usr/share/kaptan/images/kaptan_welcome.svg"))
        kaptan_logo.setAlignment(Qt.AlignRight)
        kaptan_logo.setFixedSize(196, 196)
        hlayout.addWidget(kaptan_logo)
        vlayout.addLayout(hlayout)

        vlayout.addItem(QSpacerItem(20, 40, QSizePolicy.Preferred, QSizePolicy.Preferred))
