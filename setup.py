from setuptools import setup, find_packages
from distutils.command.install import install
import os, shutil

class Install(install):
    def run(self):
        dirPath = os.path.dirname(__file__)

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

        os.chmod("script/kaptan", 0o755)
        shutil.copy("script/kaptan", "/usr/bin")

        os.system("cp -R languages {}".format(project_dir))
        os.system("cp -R data {}".format(project_dir))
        os.system("cp -R kaptan {}".format(project_dir))

        docs = ["AUTHORS", "kaptan.pro", "kaptan.qrc", "LICENSE", "MANIFEST.in", "README", "TODO"]

        for doc in docs:
            shutil.copy(doc, project_dir)



setup(
    name = "kaptan",
    packages = find_packages(),
    package_data = {os.path.dirname(__file__) : ["languages/*", "data/images/*" ,"data/*"]},
    scripts = ["script/kaptan"],
    version = "1.0",
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
    cmdclass = {'install': Install}

)
