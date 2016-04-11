from setuptools import setup
from distutils.command.install import install
from distutils.command.build import build
import os, shutil
from os.path import abspath, dirname

class Build(build):
    def run(self):
        # Clear all
        os.system("rm -rf build")

        # Copy icons
        print("Copying Images...")
        os.system("cp -R data/ build/")


        # Copy languages
        print("Copying Languages File...")
        os.system("cp -R languages/ build/")

        # Copy codes
        print("Copying PYs...")
        os.system("cp -R kaptan/ build/")


        shutil.copy("kaptan.py", "build/")
        shutil.copy("rc_kaptan.py", "build/")

class Install(install):
    def run(self):
        install.run(self)
        dirPath = dirname(abspath(__file__))

        autostart_dir = os.path.join(os.environ["HOME"], "config5","autostart")
        project_dir = "/usr/lib/kaptan"
        pixmap_dir = "/usr/share/pixmaps"
        applications_dir = "/usr/share/applications"
        icon = os.path.join(dirPath, "data", "images", "kaptan-icon.png")

        try:
            os.makedirs(autostart_dir)
            os.makedirs(project_dir)
        except OSError:
            pass

        shutil.copy(os.path.join(dirPath, "data", "kaptan.desktop"), autostart_dir)
        shutil.copy(os.path.join(dirPath, "data", "kaptan.desktop"), applications_dir)
        shutil.copy(icon, os.path.join(pixmap_dir, "kaptan.png"))
        shutil.copy("kaptan.py", os.path.join(project_dir, "kaptan5.py"))
        shutil.copy("rc_kaptan.py", project_dir)

        docs = ["AUTHORS", "kaptan.pro", "kaptan.qrc", "LICENSE", "MANIFEST.in", "README", "TODO"]

        for doc in docs:
            shutil.copy(doc, project_dir)



setup(
    name = "kaptan",
    package_data = {os.path.dirname(__file__) : ["languages/*", "data/images/*" ,"data/*"]},
    scripts = ["script/kaptan"],
    version = "5.0",
    license = "GPL v3",
    description = "PisiLinux desktop configurate.",
    author = "Metehan Özbek",
    author_email = "mthnzbk@gmail.com",
    url = "https://github.com/PisiLinuxNew/kaptan",
    keywords = ["PyQt5"],
    classifiers = [
        "Environment :: X11 Applications :: Qt",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU Affero General Public License v3",
    ],
    cmdclass = {"build" : Build,
                'install': Install}

)

