#!/usr/bin/env python
__title__       = "YSFlight DAT Compatibility Checker"
__author__      = "Decaff_42"
__version__     = "0.1"
__copyright__   = "2018 by Decaff_42"
__contact__     = "decaff_42 on ysfhq.com"
__license__     = "GNU GPLv3"
__date__        = "20 August 2018"


"""
HOW TO START:
(1) Open this script file.
(2) Press F5, or go to Run -> Run Module.
(3) Select a DAT File
(4) Select YSFlight Version
(5) Press "Check DAT" Button to run.
"""

from tkinter import *
from lib.gui_main import YSFDATCHECKER


def StartUpMessage():
    """Print the basic startup message in the command line window."""
    print("-------------------------------------------------")
    print(__title__)
    print("Version:       "+__version__)
    print("By:            "+__author__)
    print("Copyright (c)  "+__copyright__)
    print("Licensed under "+__license__)
    print("-------------------------------------------------")


def main():
    StartUpMessage()

    root = Tk()
    root.withdraw()    

    admin = [__title__,__author__,__version__,__copyright__,
             __contact__,__license__,__date__]

    YSFDATCHECKER(root, admin)

    root.deiconify()
    root.lift()
    root.attributes('-topmost',True)
    root.after_idle(root.attributes,'-topmost',False)
    root.mainloop()    


if __name__ == "__main__":
    main()
