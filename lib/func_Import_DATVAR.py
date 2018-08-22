"""Import DATVAR.csv file and parse into Dictionary"""


import os
import csv

def ImportDATVAR():
    """Import the CSV File that contains all DAT Variables available in STOCK
    DAT files from different versions of YSFlight.
    """
    fpath = os.path.join(os.getcwd(),"lib","files","DATVAR.csv")
##    path = os.path.normpath("lib\\files\\DATVAR.csv")
    DATVAR = {}
    with open(fpath,'r',newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            DATVAR[row[0]] = row[1:]

    versions = sorted(list(DATVAR.keys()))
    
    return DATVAR, versions
