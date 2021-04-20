import os as os
import sys as sys
import glob
import atexit
from pathlib import Path
import Scan
import ProcessFiles

file_extension = ""
file_list = Scan.files_list

def main():

    print("Delete.* version 0.1 ready \n")
    print("Please remember this program will delete ALL files with selected extension within this folder and it subfolders! \n")
    print("This tool removes files WITHOUT moving them to recycle bin!")
    
    UserDecision()
    ProcessFiles.DeleteFiles(Scan.files_list, file_extension)

def UserDecision():
    global file_extension
    file_extension = input("Which extension you want to delete? \n")
    if file_extension == "":
        print("No extension was provided!")
        UserDecision()
    elif len(file_extension) < 3:
        print("Extension is not valid! Less than 3 characters.")
        UserDecision()
    elif len(file_extension) >3:
        print("Too many characters!")
        UserDecision()
    else:
        print("Scanning for files. Please wait \n")
        Scan.scanForFiles(file_extension)


def exitApp():
    print("Shutting down...")

atexit.register(exitApp)

if __name__==__name__:
    main()