# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import lazy_setting



setup(
    name="lazy_setting",
    version= lazy_setting.__version__,
    url = "https://github.com/wcsjtu/lazy_settings",
    description = "lazy setting module from django, support python 2.7 only",
    author = lazy_setting.__author__,
    maintainer = lazy_setting.__author__,
    maintainer_email = lazy_setting.__author__ + "@gmail.com",
    license = "MIT",
    packages = find_packages()
    )