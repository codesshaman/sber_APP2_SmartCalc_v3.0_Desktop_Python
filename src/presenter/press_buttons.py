from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication
from main import check_debug
# from views import SimpleButton

debug = check_debug()
def press_button():
    if debug:
        print("Press")