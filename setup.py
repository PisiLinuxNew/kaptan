# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 3 of the License, or (at your option)
# any later version.
#
# Please read the docs/COPYING file.
#

from setuptools import setup, find_packages
from os import listdir, system


langs = []
for l in listdir('languages'):
    if l.endswith('ts'):
        system('lrelease-qt5 languages/%s' % l)
        langs.append(('languages/%s' % l).replace('.ts', '.qm'))


system('pyrcc5 kaptan.qrc -o kaptan5/rc_kaptan.py')

datas = [('/usr/share/applications', ['data/kaptan.desktop']),
         ('/etc/skel/.config5/autostart', ['data/kaptan.desktop']),
         ('/usr/share/icons/hicolor/64x64/apps', ['data/images/kaptan-icon.png']),
         ('/usr/share/kaptan/languages', langs)]

setup(
    name = "kaptan",
    scripts = ["script/kaptan"],
    packages = find_packages(),
    version = "5.0",
    license = "GPL v3",
    description = "PisiLinux desktop configurate.",
    author = "Metehan Özbek",
    author_email = "mthnzbk@gmail.com",
    url = "https://github.com/PisiLinuxNew/kaptan",
    keywords = ["PyQt5"],
    data_files = datas
)

