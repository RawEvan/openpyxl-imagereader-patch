#-*- coding:utf-8 -*-


from setuptools import setup, find_packages

setup(
    name = "openpyxl_image_patch",
    version = "0.1.0",
    keywords = ("openpyxl", "excel","image"),
    description = "Patch for openpyxl to reserver images",
    long_description = "Patch for openpyxl to reserver images",
    license = "MIT Licence",

    url = "https://github.com/RawEvan/openpyxl_image_patch",
    author = "Evan",
    author_email = "evan.li@gllue.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ['openpyxl>=2.5.4']
)

