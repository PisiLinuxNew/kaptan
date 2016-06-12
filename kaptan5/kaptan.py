#!/usr/bin/env python3

import sys, os
from PyQt5.QtCore import QTranslator, QLocale, Qt, QProcess, pyqtSignal
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QWizard, QApplication, QDesktopWidget, qApp
from kaptan5 import rc_kaptan
from kaptan5.libkaptan import *


class Kaptan(QWizard):
    def __init__(self):
        super().__init__()
        self.setObjectName("wizard")
        self.setWindowTitle(self.tr("Kaptan Desktop"))
        self.setWindowIcon(QIcon.fromTheme("kaptan-icon"))
        self.setMinimumSize(900, 650)
        self.setMaximumSize(1050, 720)
        x = (QDesktopWidget().screen().width() - self.width())/2
        y = (QDesktopWidget().screen().height() - self.height())/2
        self.move(x, y)
        self.setPixmap(QWizard.LogoPixmap, QPixmap(":/data/images/kaptan-logo.png"))

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

        self.button(QWizard.FinishButton).setObjectName("push_button")
        self.button(QWizard.NextButton).setObjectName("push_button")
        self.button(QWizard.CancelButton).setObjectName("push_button")
        self.button(QWizard.BackButton).setObjectName("push_button")

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
    app.setApplicationVersion("5.0 Beta4")

    locale = QLocale.system().name()
    translator = QTranslator(app)
    translator.load("/usr/share/kaptan/languages/{}.qm".format(locale))
    app.installTranslator(translator)

    kaptan = Kaptan()
    kaptan.show()

    file = open(os.path.join("/usr/share/kaptan", "data/kaptan.css"))
    qApp.setStyleSheet(file.read())

    app.exec_()

if __name__ == "__main__":
    main()
