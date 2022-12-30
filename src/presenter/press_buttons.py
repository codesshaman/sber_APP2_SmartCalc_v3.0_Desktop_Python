import tkinter as tk
from main import check_debug
from views import buttons_views

debug = check_debug()
def press_button():
    if debug:
        print("Press")
