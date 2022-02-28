import datetime
import os.path as path

FILENAME = "dennikhovorov.log"
__LOG_INIT = False

def init():
    f = open(FILENAME,("a" if path.exists(FILENAME) else "w"))
    f.write("---- log -----\n")
    f.close()

def write(text):
    global __LOG_INIT
    if not __LOG_INIT:
        init()
        __LOG_INIT = True
    f = open(FILENAME,"a")
    msg = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S") + " --> " + text + "\n"
    f.write(msg)
    f.close()