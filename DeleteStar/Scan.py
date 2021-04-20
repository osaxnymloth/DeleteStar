import os as os




files_list = []

def scanForFiles(extension):


    print("Checking for files with selected extension: " + extension)
    if not files_list: #is the list empty?
        print("Currently no files in the list, adding")
        for root, dirs, files in os.walk(os.getcwd()):
            for file in files:
                if file.endswith(extension):
                    files_list.append(file)
        if not files_list:
            print("List is empty. No files with provided extension were detected. \n")
        else:
            print("Detected # of files: ", len(files_list))
            print("List: ")
            print(files_list)
        print("End of the list of files. \n")
    elif files_list: #if list is not empty, it must been populated already!
        print("Files already detected, doing nothing.")



