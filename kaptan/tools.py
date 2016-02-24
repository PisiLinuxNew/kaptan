import re

data = """[ActionPlugins][0]
MidButton;NoModifier=org.kde.paste
RightButton;NoModifier=org.kde.contextmenu
wheel:Vertical;NoModifier=org.kde.switchdesktop

[ActionPlugins][1]
RightButton;NoModifier=org.kde.contextmenu

[ActionPlugins][127]
RightButton;NoModifier=org.kde.contextmenu

[Containments]
AppletOrder=2
Image=file:///usr/share/wallpapers/Kite/contents/images/800x600.jpg
activityId=782e3974-9f83-40bd-b1a4-165f60c3aa75
extraItems=org.kde.plasma.volume, org.kde.plasma.notifications, org.kde.discovernotifier, org.kde.plasma.mediacontroller, org.kde.plasma.battery, org.kde.plasma.bluetooth, org.kde.plasma.clipboard, org.kde.plasma.networkmanagement, org.kde.plasma.devicenotifier
favorites=preferred://browser, systemsettings.desktop, org.kde.dolphin.desktop, org.kde.kate.desktop
formfactor=0
global=Alt+F1
height=768
immutability=1
knownItems=org.kde.plasma.volume, org.kde.plasma.notifications, org.kde.discovernotifier, org.kde.plasma.mediacontroller, org.kde.plasma.battery, org.kde.plasma.bluetooth, org.kde.plasma.clipboard, org.kde.plasma.networkmanagement, org.kde.plasma.devicenotifier
lastScreen=0
location=0
plugin=org.kde.plasma.desktop
wallpaperplugin=org.kde.image
width=1366

[Containments][1]
activityId=
formfactor=2
immutability=1
lastScreen=0
location=4
plugin=org.kde.panel
wallpaperplugin=org.kde.image

[Containments][1][Applets][2]
immutability=1
plugin=org.kde.plasma.kickoff

[Containments][1][Applets][2][Configuration][General]
favorites=preferred://browser,systemsettings.desktop,org.kde.dolphin.desktop,org.kde.kate.desktop

[Containments][1][Applets][2][Configuration][Shortcuts]
global=Alt+F1

[Containments][1][Applets][2][Shortcuts]
global=Alt+F1

[Containments][1][Applets][3]
immutability=1
plugin=org.kde.plasma.pager

[Containments][1][Applets][4]
immutability=1
plugin=org.kde.plasma.taskmanager

[Containments][1][Applets][5]
immutability=1
plugin=org.kde.plasma.systemtray

[Containments][1][Applets][5][Configuration][Containments][8]
formfactor=2
location=4

[Containments][1][Applets][5][Configuration][Containments][8][Applets][10]
immutability=1
plugin=org.kde.plasma.devicenotifier

[Containments][1][Applets][5][Configuration][Containments][8][Applets][11]
immutability=1
plugin=org.kde.plasma.notifications

[Containments][1][Applets][5][Configuration][Containments][8][Applets][12]
immutability=1
plugin=org.kde.plasma.clipboard

[Containments][1][Applets][5][Configuration][Containments][8][Applets][13]
immutability=1
plugin=org.kde.discovernotifier

[Containments][1][Applets][5][Configuration][Containments][8][Applets][14]
immutability=1
plugin=org.kde.plasma.battery

[Containments][1][Applets][5][Configuration][Containments][8][Applets][15]
immutability=1
plugin=org.kde.plasma.bluetooth

[Containments][1][Applets][5][Configuration][Containments][8][Applets][16]
immutability=1
plugin=org.kde.plasma.networkmanagement

[Containments][1][Applets][5][Configuration][Containments][8][Applets][9]
immutability=1
plugin=org.kde.plasma.volume

[Containments][1][Applets][5][Configuration][General]
extraItems=org.kde.plasma.volume,org.kde.plasma.notifications,org.kde.discovernotifier,org.kde.plasma.mediacontroller,org.kde.plasma.battery,org.kde.plasma.bluetooth,org.kde.plasma.clipboard,org.kde.plasma.networkmanagement,org.kde.plasma.devicenotifier
knownItems=org.kde.plasma.volume,org.kde.plasma.notifications,org.kde.discovernotifier,org.kde.plasma.mediacontroller,org.kde.plasma.battery,org.kde.plasma.bluetooth,org.kde.plasma.clipboard,org.kde.plasma.networkmanagement,org.kde.plasma.devicenotifier

[Containments][1][Applets][6]
immutability=1
plugin=org.kde.plasma.digitalclock

[Containments][1][General]
AppletOrder=2;3;4;5;6

[Containments][7]
activityId=782e3974-9f83-40bd-b1a4-165f60c3aa75
formfactor=0
immutability=1
lastScreen=0
location=0
plugin=org.kde.desktopcontainment
wallpaperplugin=org.kde.image

[Containments][7][Wallpaper][org.kde.image][General]
height=768
width=1366

"""

def getMenuStyle(data):
    regex = "(\[Containments\]\[([1-9])\]\[Applets\]\[([1-9])\]\nimmutability=1\nplugin=(.*)\n)"

    read = re.search(regex, data)

    if read:
        return read.group(1), read.group(2), read.group(3), read.group(4)

def setMenuStyle(data, style):
    regex = r"\[Containments\]\[%s\]\[Applets\]\[%s\]\nimmutability=.\nplugin=(.*)\n"%(getMenuStyle(data)[1],
                                                                                                 getMenuStyle(data)[2])

    com = re.compile(regex)

    return com.sub(getMenuStyle(data)[0].replace(getMenuStyle(data)[3], style), data)

def getDesktopView(data):
    regex = "(\[Containments\]\[[1-9]*\]\nactivityId=.+\n.*\n.*\nlastScreen=.*\n.*\nplugin=(.*)\n)"

    read = re.search(regex, data)

    if read:
        return read.group(1), read.group(2)

def setDesktopView(data, view):
    regex = "\[Containments\]\[[1-9]*\]\nactivityId=.+\n.*\n.*\nlastScreen=.*\n.*\nplugin=(.*)\n"

    com = re.compile(regex)

    return com.sub(getDesktopView(data)[0].replace(getDesktopView(data)[1], view), data)


def getWallpaperGroup(data):
    regex = "(\[Containments\]\[[1-9]+\]\[Wallpaper\]\[org.kde.image\]\[General\]\n(.*)=(.*)\n)"

    read = re.search(regex, data)

    if read:
        if read.group(2) != "Image":
            regex = "(\[Containments\]\[[1-9]+\]\[Wallpaper\]\[org.kde.image\]\[General\]\n)((.*)=.*\n.*\n)"

            read = re.search(regex, data)

            if read:
                return read.group(1), read.group(2), read.group(3)

        return read.group(1), read.group(2), read.group(3)


def setWallpaperGroup(data, path):
    if getWallpaperGroup(data)[1] != "Image":
        regex = "\[Containments\]\[[1-9]+\]\[Wallpaper\]\[org.kde.image\]\[General\]\n.*\n.*\n"
        com = re.compile(regex)

        return com.sub((getWallpaperGroup(data)[0]+"Image=%s\n"+getWallpaperGroup(data)[1])%path, data)
    else:
        regex = r"\[Containments\]\[[1-9]+\]\[Wallpaper\]\[org.kde.image\]\[General\]\n%s=.*\n"%(getWallpaperGroup(data)[1])

        com = re.compile(regex)

        return com.sub(getWallpaperGroup(data)[0].replace(getWallpaperGroup(data)[2], path), data)





#print(getMenuStyle(data))
#print(setMenuStyle(data))
#print(getDesktopStyle(data))
#print(setDesktopStyle(data))
#print(getWallpaperGroup(data))
#print(setWallpaperGroup(data, "met2ehan.png"))