import re

data = """[ActionPlugins][0]
MidButton;NoModifier=org.kde.paste
RightButton;NoModifier=org.kde.contextmenu
wheel:Vertical;NoModifier=org.kde.switchdesktop

[AppletGlobals][org.kde.plasma.notifications]
popupPosition=0

[Containments][1]
activityId=
formfactor=2
immutability=1
lastScreen=0
location=4
plugin=org.kde.panel
wallpaperplugin=org.kde.image

[Containments][1][Applets][31][Configuration][General]
favoriteApps=preferred://browser,systemsettings.desktop,org.kde.dolphin.desktop,org.kde.kate.desktop

[Containments][1][Applets][32]
immutability=1
plugin=org.kde.plasma.kickoff

[Containments][1][Applets][32][Configuration][General]
favoriteApps=preferred://browser,systemsettings.desktop,org.kde.dolphin.desktop,org.kde.kate.desktop

[Containments][38]
activityId=1073333c-eb01-4786-b734-55fd1a3be375
formfactor=0
immutability=1
lastScreen=-1
location=0
plugin=org.kde.plasma.folder
wallpaperplugin=org.kde.image

[Containments][38][ConfigDialog]
DialogHeight=480
DialogWidth=640

[Containments][38][Wallpaper][org.kde.image][General]
Image=file:///usr/share/wallpapers/Auros/contents/images/5408x3464.png
height=768
width=1366

[General]
immutability=1
"""

def getMenuStyle(data):
    regex = "(\[Containments\]\[[1-9]*\]\[Applets\]\[[1-9]*\]\nimmutability=.\nplugin=(.*)\n)"

    read = re.search(regex, data)

    if read:
        return read.group(1), read.group(2)

def setMenuStyle(data):
    regex = "\[Containments\]\[[1-9]*\]\[Applets\]\[[1-9]*\]\nimmutability=.\nplugin=(.*)\n"

    com = re.compile(regex)

    return com.sub(getMenuStyle(data)[0].replace(getMenuStyle(data)[1], "org.kde.plasma.kicker"), data)

def getDesktopStyle(data):
    regex = "(\[Containments\]\[[1-9]*\]\nactivityId=.+\n.*\n.*\nlastScreen=.*\n.*\nplugin=(.*)\n)"

    read = re.search(regex, data)

    if read:
        return read.group(1), read.group(2)

def setDesktopStyle(data):
    regex = "\[Containments\]\[[1-9]*\]\nactivityId=.+\n.*\n.*\nlastScreen=.*\n.*\nplugin=(.*)\n"

    com = re.compile(regex)

    return com.sub(getDesktopStyle(data)[0].replace(getDesktopStyle(data)[1], "org.kde.plasma.desktop"), data)


#print(getMenuStyle(data))
#print(setMenuStyle(data))
#print(getDesktopStyle(data))
#print(setDesktopStyle(data))