import os
import shutil
from tkinter import E

def updateNamesOfFilesInDirectory(fileDirectoryFolder, fileDestination): #this process gets the source from the user, processes it, and sends to destination

    path = fileDirectoryFolder #this is your source directory    
    os.chdir(path)
    preFix = os.getcwd() #get the current directory
    preFix = preFix.rsplit('\\',1)[1] #get the current folder
    preFix = processFileName(preFix) #get the name of the current directory, this will be used to create a preFix for the file

    i = 0
    for fileName in os.listdir(path): #
        extractedFileName = os.path.splitext(fileName)[0] #extract the file name from the file
        extractedFileName = processFileName(extractedFileName) #run the file name through the processFileName function
        extractedFileNameExtension = os.path.splitext(fileName)[1] #pull the file extension
        newFileName = fileDestination + "\\" + preFix + "_" + str(extractedFileName) + extractedFileNameExtension # combine the file name and put the directory in front of the file name so it sends the file to that direction
        shutil.copy2(fileName, newFileName ) #copy the file from the source and send the file processed to the destination        

        
def processFileName(fileName): #processes file name to be easily readable by sharepoint - maybe
    fileName = fileName.replace(" ", "-") #remove spaces and turn into -
    fileName = fileName.replace("_", "-") #remove _ and turn into -
    return fileName