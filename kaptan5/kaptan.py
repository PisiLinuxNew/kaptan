#!/usr/bin/env python3
#
#
#  Copyright 2016 Metehan Özbek <mthnzbk@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import sys, os
from PyQt5.QtCore import QTranslator, QLocale, Qt, QProcess, pyqtSignal
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QWizard, QApplication, QDesktopWidget
from kaptan5 import rc_kaptan
from kaptan5.libkaptan import *


class Kaptan(QWizard):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(self.tr("Kaptan Desktop"))
        self.setWindowIcon(QIcon.fromTheme("kaptan-icon"))
        self.setMinimumSize(850, 600)
        self.setMaximumSize(950, 620)
        x = (QDesktopWidget().screen().width() - self.width())/2
        y = (QDesktopWidget().screen().height() - self.height())/2
        self.move(x, y)
        self.setPixmap(QWizard.LogoPixmap, QPixmap(":/data/images/kaptan.png"))

        self.setButtonText(QWizard.NextButton, self.tr("Next"))
        self.button(QWizard.NextButton).setIcon(QIcon.fromTheme("arrow-right"))
        self.button(QWizard.NextButton).setLayoutDirection(Qt.RightToLeft)

        self.setButtonText(QWizard.CancelButton, self.tr("Cancel"))
        self.button(QWizard.CancelButton).setIcon(QIcon.fromTheme("dialog-cancel"))
        self.setOption(QWizard.NoCancelButtonOnLastPage, True)
        self.setOption(QWizard.CancelButtonOnLeft, True)

        self.setButtonText(QWizard.BackButton, self.tr("Back"))
        self.setOption(QWizard.NoBackButtonOnLastPage, True)
        self.setOption(QWizard.NoBackButtonOnStartPage, True)
        self.button(QWizard.BackButton).setIcon(QIcon.fromTheme("arrow-left"))

        self.setButtonText(QWizard.FinishButton, self.tr("Finish"))
        self.button(QWizard.FinishButton).setIcon(QIcon.fromTheme("dialog-ok-apply"))


        self.addPage(WelcomeWidget(self))
        self.addPage(MouseWidget(self))
        self.addPage(ThemeWidget(self))
        self.addPage(MenuWidget(self))
        self.addPage(WallpaperWidget(self))
        self.addPage(AvatarWidget(self))
        #self.addPage(PMWidget()) FIXME
        self.sumId = self.addPage(SummaryWidget(self))
        self.otherId = self.addPage(OtherWidget(self))

        self.currentIdChanged.connect(self.optionsAccepted)
        self.button(QWizard.FinishButton).clicked.connect(self.close)

    summaryVisible = pyqtSignal()
    def optionsAccepted(self, id):
        if id == self.otherId:

            #MouseWidget
            self.page(1).execute()
            #ThemeWidget
            self.page(2).execute()
            #MenuWidget
            self.page(3).execute()
            #WallpaperWidget
            self.page(4).execute()
            #AvatarWidget
            self.page(5).execute()


            p = QProcess()
            p.startDetached("killall plasmashell")
            p.waitForStarted(2000)
            p.startDetached("kstart5 plasmashell")

        if id == self.sumId:
            self.setButtonText(QWizard.NextButton, self.tr("Apply Settings"))
            self.button(QWizard.NextButton).setIcon(QIcon.fromTheme("dialog-ok-apply"))
            self.summaryVisible.emit()
        else:
            self.setButtonText(QWizard.NextButton, self.tr("Next"))
            self.button(QWizard.NextButton).setIcon(QIcon.fromTheme("arrow-right"))

    def closeEvent(self, event):
        desktop_file = os.path.join(os.environ["HOME"], ".config", "autostart", "kaptan.desktop")
        if os.path.exists(desktop_file):
            os.remove(desktop_file)


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Kaptan")
    app.setOrganizationName("Kaptan")
    app.setApplicationVersion("5.0 Beta3")
    #app.setStyleSheet(open(join(dirPath, "data/libkaptan.qss").read())

    locale = QLocale.system().name()
    translator = QTranslator(app)
    translator.load("/usr/share/kaptan/languages/{}.qm".format(locale))
    app.installTranslator(translator)

    kaptan = Kaptan()
    kaptan.show()
    app.exec_()

if __name__ == "__main__":
    main()
