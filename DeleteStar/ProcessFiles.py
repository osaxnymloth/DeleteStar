import os as os
import sys as sys
import glob
from pathlib import Path

file_list = []
extension = ""

def DeleteFiles(file_list, extension):
    files_to_delete = file_list
    f_text = open("log.txt", "w+")
    if not file_list:
        print("Detected no files! Quitting!")
        
    else:
        user_confirmation = input("Are you sure you want to continue? Y or N \n")
        if user_confirmation == "n":
            print("Abandoning!")
            sys.exit("...")
        if user_confirmation == "y":
            print("Progressing!")
            for root, dirs, files in os.walk(os.getcwd()):
                for file in files:
                    if file.endswith(extension):
                        source_file = os.path.join(root, file)
                        f_text.write("File: " + source_file + " \n")
                        os.remove(source_file)
            f_text.close()
            print("Done! See log.txt for details.")
        else:
            print("Wrong input! Shutting down for safety!")

