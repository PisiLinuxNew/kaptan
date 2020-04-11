#!/usr/bin/env python3
#
#  Copyright 2016 Metehan Özbek <mthnzbk@gmail.com>
#            2020 Erdem Ersoy <erdemersoy@erdemersoy.net>
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

import subprocess
from setuptools import setup, find_packages
from os import listdir
from kaptan.libkaptan.version import Version

langs = []
for langfile in listdir("languages"):
    if langfile.endswith("ts"):
        subprocess.run(["lrelease", "languages/{}".format(langfile)])
        langs.append("languages/{}".format(langfile).replace(".ts", ".qm"))

subprocess.run(["pyrcc5", "kaptan.qrc", "-o", "kaptan5/rc_kaptan.py"])

datas = [("/usr/share/applications", ["data/kaptan.desktop"]),
         # Kaptan will be started via Pisi Linux Welcome Application
         # ("/etc/skel/.config/autostart", ["data/kaptan.desktop"]),
         ("/usr/share/icons/hicolor/scalable/apps", ["data/images/kaptan-icon.svg"]),
         ("/usr/share/kaptan/languages", langs)]

setup(
    name="kaptan",
    scripts=["script/kaptan"],
    packages=find_packages(),
    version=Version.getVersion(),
    license="GPLv3",
    description="Pisi Linux quick desktop configuraton tool.",
    author="Metehan Özbek",
    author_email="mthnzbk@gmail.com",
    url="https://github.com/PisiLinuxNew/kaptan",
    keywords=["PyQt5"],
    data_files=datas
)
