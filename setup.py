#!/usr/bin/env python
from setuptools import setup, find_packages
 
setup (
    name = "Gryphus Python Utils",
    version = "1.0",
    description="Python util libraries for other projects",
    author="Mario Rivas",
    author_email="h@cked.es", 
    url="https://github.com/gry/utils",
    # packages=['tunnelling'],
    packages=find_packages(),
    download_url = "https://github.com/gry/utils",
    zip_safe = True,
    # install_requires = ['paramiko >= 1.7.7.1']
)



