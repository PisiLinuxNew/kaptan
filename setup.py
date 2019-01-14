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

from setuptools import setup, find_packages
from os import listdir, system


langs = []
for l in listdir('languages'):
    if l.endswith('ts'):
        #Temporary bindir to avoid qt4 conflicts
        #system('lrelease-qt5 languages/%s' % l)
        system('lrelease languages/%s' % l)
        langs.append(('languages/%s' % l).replace('.ts', '.qm'))


system('pyrcc5 kaptan.qrc -o kaptan5/rc_kaptan.py')

datas = [('/usr/share/applications', ['data/kaptan.desktop']),
         # welcome uygulaması ile başlatılacak.
         #('/etc/skel/.config/autostart', ['data/kaptan.desktop']),
         ('/usr/share/icons/hicolor/scalable/apps', ['data/images/kaptan-icon.svg']),
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

