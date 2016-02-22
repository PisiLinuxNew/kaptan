#!/usr/bin/env python3

import sys
import rc_kaptan
from kaptan import *
from PyQt5.QtWidgets import QWizard, QApplication
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QTranslator, QLocale, Qt, QProcess

class Kaptan(QWizard):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kaptan Masaüstü")
        self.setWindowIcon(QIcon(":/data/images/kaptan-icon.png"))
        self.setMinimumSize(900, 640)
        self.setMaximumSize(1000, 650)
        self.move(0,0)
        self.setPixmap(QWizard.LogoPixmap, QPixmap(":/data/images/kaptan-logo.png"))

        self.setButtonText(QWizard.NextButton, self.tr("Next"))
        self.button(QWizard.NextButton).setIcon(QIcon(":/data/images/arrow-right.png"))
        self.button(QWizard.NextButton).setLayoutDirection(Qt.RightToLeft)

        self.setButtonText(QWizard.CancelButton, self.tr("Cancel"))
        self.button(QWizard.CancelButton).setIcon(QIcon(":/data/images/cross.png"))
        self.setOption(QWizard.NoCancelButtonOnLastPage, True)
        self.setOption(QWizard.CancelButtonOnLeft, True)

        self.setButtonText(QWizard.BackButton, self.tr("Back"))
        self.setOption(QWizard.NoBackButtonOnLastPage, True)
        self.setOption(QWizard.NoBackButtonOnStartPage, True)
        self.button(QWizard.BackButton).setIcon(QIcon(":/data/images/arrow-left.png"))

        self.setButtonText(QWizard.FinishButton, self.tr("Finish"))
        self.button(QWizard.FinishButton).setIcon(QIcon(":/data/images/tick.png"))



        self.addPage(WelcomeWidget())
        self.addPage(MouseWidget())
        self.addPage(ThemeWidget())
        self.addPage(MenuWidget())
        self.addPage(WallpaperWidget())
        self.addPage(AvatarWidget())
        #self.addPage(PMWidget()) FIXME
        self.sumId = self.addPage(SummaryWidget())
        self.otherId = self.addPage(OtherWidget())

        self.currentIdChanged.connect(self.optionsAccepted)

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


            proc1 = QProcess()
            proc2 = QProcess()

            proc1.startDetached("killall plasmashell")
            proc2.waitForStarted(2000)
            proc2.startDetached("kstart plasmashell")
             # execute() methodları sırayla çalışacak ve plasma kill sonra start
        if id == self.sumId:
            self.setButtonText(QWizard.NextButton, self.tr("Apply Settings"))
        else:
            self.setButtonText(QWizard.NextButton, self.tr("Next"))


def main():
    app = QApplication(sys.argv)
    #app.setStyleSheet(open("data/kaptan.qss").read())

    locale = QLocale.system().name()
    translator = QTranslator(app)
    app.installTranslator(translator)

    kaptan = Kaptan()
    kaptan.show()
    app.exec_()

if __name__ == "__main__":
    main()