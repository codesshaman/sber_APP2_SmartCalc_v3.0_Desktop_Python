######################
# Install on MacOS X #
######################
from setuptools import setup

APP_NAME = 'SmartCalc_v3'
APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'iconfile: icon.icns'
}

setup(
    app=APP,
    name=APP_NAME,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

######################
# Install on Windows #
######################


######################
# Install on Linux   #
######################