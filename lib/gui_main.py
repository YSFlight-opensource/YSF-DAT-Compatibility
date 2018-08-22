from tkinter import *
from tkinter import messagebox
import time
import os

from lib.func_Import_DATVAR import ImportDATVAR

class YSFDATCHECKER(Frame):
    def __init__(self,parent,admin):
        super().__init__(parent)
        self.parent     = parent
        self.title      = admin[0]
        self.author     = admin[1]
        self.version    = admin[2]
        self.copy_right = admin[3]
        self.contact    = admin[4]
        self.license    = admin[5]
        self.date       = admin[6]

        self.CreateVars()
        self.setupUI()


    def CreateVars(self):
        """Create Variables that need to be initialized before the GUI"""
        self.dat_path = StringVar()
        self.dat_path.set("")

        self.YSF_Version = StringVar()
        self.YSF_Version.set("20170314")

        self.ysf_versions = ["20170314","20150406","20130817","20120701",
                             "20110207","20100331","20090611","20080220",
                             "20070415","20060828"]


    def setupUI(self):
        """Create the GUI"""

        # Title
        title = "YSFlight DAT Compatibility Checker v{}".format(self.version)
        self.parent.wm_title(title)

        # Geometry
        self.parent.wm_resizable(width=False,height=False)
        self.parent.minsize(self.parent.winfo_width()+100,
                            self.parent.winfo_height())

        # Create Sub Areas
        mainframe = Frame(self.parent).pack(side=LEFT)
        topframe = Frame(mainframe)
        bottomframe = Frame(mainframe)

        self.DAT_PATH = Entry(topframe,textvar=self.dat_path,width=35)
        self.DAT_PATH.pack(side=LEFT,fill=BOTH)

        self.DAT_SEL = Button(topframe,text="Select DAT",command=self.GetDat)
        self.DAT_SEL.pack(side=LEFT,fill=BOTH)

        ver = Label(bottomframe,
                    text="Select YSF Version:").pack(side=LEFT,fill=BOTH)

        self.YSF_SEL = OptionMenu(bottomframe,
                                  self.YSF_Version,
                                  *self.ysf_versions)
        self.YSF_SEL.pack(side=LEFT,fill=BOTH,expand=TRUE)

        run = Button(mainframe,text="Check DAT",command=self.CheckDat)
        


        topframe.pack(fill=BOTH,expand=TRUE)
        bottomframe.pack(fill=BOTH,expand=TRUE)
        run.pack(side=LEFT,fill=BOTH,expand=TRUE)



    def GetDat(self):
        """Get a DAT File"""
        filename = filedialog.askopenfilename()
        if filename is not "" and filename.endswith(".dat"):
            self.dat_path.set(filename)
        else:
            print("No DAT File Selected.")
            messagebox.showinfo(title="Oops!",
                                message="No Dat File selected!")


    def ParseDat(self):
        """Import and parse a list of variablese in the DAT File"""

        # Import file and strip the '\n'
        with open(self.dat_path.get(),'r') as file:
            self.dat = file.read().splitlines()
        print("Imported {}".format(os.path.basename(self.dat_path.get())))

        # Extract variables and ignore REM and blank lines
        self.datvars = []
        for line in self.dat:
            if line.startswith("REM") or line == "":
                pass
            else:
                self.datvars.append(line[0:8])



    def CheckDat(self):
        """Compare DAT to YSFlight Versions"""

        if len(self.dat_path.get()) <= 1 :
            m = "You have not selected a DAT File. You must have a DAT file"
            m += " in order to proceed."
            messagebox.showinfo(title="ERROR!",
                                message=m)
            return

        # Import DAT File
        self.ParseDat()

        # Import DATVAR
        self.DATVAR , versions = ImportDATVAR()
        baseline = list(filter(("").__ne__,self.DATVAR[self.YSF_Version.get()]))

        over = []
        for var in self.datvars:
            if var not in baseline and var not in over:
                over.append(var)

        if "AUTOCALC" in over:
            del over[over.index("AUTOCALC")]

        print("Analyzing {} Variables".format(self.YSF_Version.get()))

        if len(over) > 0:
            m = "The following DAT Variables may be incompatible with "
            m += "{}:\n".format(self.YSF_Version.get())
            for i in over:
                m += "  {}\n".format(i)
            messagebox.showinfo(title="Incompatible Variables Found!",
                                message = m)
        
        
