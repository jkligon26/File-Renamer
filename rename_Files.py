# -*- coding: utf-8 -*-
import os
def rename_files():
    # get file names from a folder
    fileList = os.listdir(r"...") #Insert directory
   # print(fileList)
    
    savedPath = os.getcwd()
    print("Current working directory is " + savedPath)
    os.chdir(r"...") #Insert directory
    
    #for each file, rename the filename
    table = str.maketrans(dict.fromkeys("0123456789")) #removes numbers from the filename
    for fileName in fileList:
        print("Old name - " + fileName)
        print("New name - " + fileName.translate(table))
        os.rename(fileName, fileName.translate(table))
    return;
    
rename_files()
