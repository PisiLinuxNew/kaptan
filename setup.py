from setuptools import setup, find_packages

setup(
    name = "kaptan",
    packages = find_packages(),
    #package_data = {"kaptan" : ["languages/*", "images/icons/*" ,"images/*.png", "media/*"]},
    scripts = ["kaptan"],
    version = "1.0",
    license = "GPL v3",
    #description = "PisiLinux başlangıç yapılandırması.",
    author = "Metehan Özbek",
    author_email = "mthnzbk@gmail.com",
    url = "https://github.com/mthnzbk/aptan",
    download_url = "https://pypi.python.org/pypi/kaptan",
    #install_requires=["", ""],
    keywords = ["PyQt5"],
    classifiers = [
        "Environment :: X11 Applications :: Qt",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU Affero General Public License v3",
    ],

)