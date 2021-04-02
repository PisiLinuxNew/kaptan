#!/usr/bin/env python3
#
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

import sys
from PyQt5 import QtWidgets
from libkaptan import *


class Kaptan(QtWidgets.QWizard):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(self.tr("Kaptan"))
        self.setWindowIcon(QIcon.fromTheme("kaptan-icon"))
        self.setMinimumSize(850, 600)
        self.setMaximumSize(950, 620)
        x = (QtWidgets.QDesktopWidget().size().width() - self.width()) / 2
        y = (QtWidgets.QDesktopWidget().size().height() - self.height()) / 2
        self.move(x, y)
        self.setPixmap(QtWidgets.QWizard.LogoPixmap, QPixmap("/usr/share/kaptan/images/kaptan.png"))

        self.setButtonText(QtWidgets.QWizard.NextButton, self.tr("Next"))
        self.button(QtWidgets.QWizard.NextButton).setIcon(QIcon.fromTheme("arrow-right"))
        self.button(QtWidgets.QWizard.NextButton).setLayoutDirection(Qt.RightToLeft)

        self.setButtonText(QtWidgets.QWizard.CancelButton, self.tr("Cancel"))
        self.button(QtWidgets.QWizard.CancelButton).setIcon(QIcon.fromTheme("dialog-cancel"))
        self.setOption(QtWidgets.QWizard.NoCancelButtonOnLastPage, True)
        self.setOption(QtWidgets.QWizard.CancelButtonOnLeft, True)

        self.setButtonText(QtWidgets.QWizard.BackButton, self.tr("Back"))
        self.setOption(QtWidgets.QWizard.NoBackButtonOnLastPage, True)
        self.setOption(QtWidgets.QWizard.NoBackButtonOnStartPage, True)
        self.button(QtWidgets.QWizard.BackButton).setIcon(QIcon.fromTheme("arrow-left"))

        self.setButtonText(QtWidgets.QWizard.FinishButton, self.tr("Finish"))
        self.button(QtWidgets.QWizard.FinishButton).setIcon(QIcon.fromTheme("dialog-ok-apply"))

        self.addPage(WelcomeWidget(self))
        self.addPage(MouseWidget(self))
        self.addPage(ThemeWidget(self))
        self.addPage(MenuWidget(self))
        self.addPage(WallpaperWidget(self))
        self.addPage(AvatarWidget(self))
        self.sumId = self.addPage(SummaryWidget(self))
        self.otherId = self.addPage(OtherWidget(self))

        self.currentIdChanged.connect(self.optionsAccepted)
        self.button(QtWidgets.QWizard.FinishButton).clicked.connect(self.close)

    summaryVisible = pyqtSignal()

    def optionsAccepted(self, identity):
        if identity == self.otherId:
            # MouseWidget
            self.page(1).execute()
            # ThemeWidget
            self.page(2).execute()
            # MenuWidget
            self.page(3).execute()
            # WallpaperWidget
            self.page(4).execute()
            # AvatarWidget
            self.page(5).execute()

            p = QProcess()
            p.startDetached("kquitapp5 plasmashell")
            p.waitForStarted(2000)
            p.startDetached("kstart5 plasmashell")

        if identity == self.sumId:
            self.setButtonText(QtWidgets.QWizard.NextButton, self.tr("Apply Settings"))
            self.button(QtWidgets.QWizard.NextButton).setIcon(QIcon.fromTheme("dialog-ok-apply"))
            self.summaryVisible.emit()
        else:
            self.setButtonText(QtWidgets.QWizard.NextButton, self.tr("Next"))
            self.button(QtWidgets.QWizard.NextButton).setIcon(QIcon.fromTheme("arrow-right"))

    def closeEvent(self, event):
        desktop_file = os.path.join(os.environ["HOME"], ".config", "autostart", "kaptan.desktop")
        if os.path.exists(desktop_file):
            os.remove(desktop_file)


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("Kaptan")
    app.setOrganizationName("Kaptan")
    app.setApplicationVersion(Version.getVersion())
    # app.setStyleSheet(open(join(dirPath, "data/libkaptan.qss").read())

    locale = QLocale.system().name()
    translator = QTranslator(app)
    translator.load("/usr/share/kaptan/languages/{}.qm".format(locale))
    app.installTranslator(translator)

    kaptan = Kaptan()
    kaptan.show()
    app.exec_()


if __name__ == "__main__":
    main()
