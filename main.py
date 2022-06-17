import os
import shutil
from tkinter import E
from functions import updateNamesOfFilesInDirectory, processFileName

#this software adds the immediate folder directory as a prefix to the file
#example file source >> N:\Equipment\F\FO-FORMING\FO-52\Manual\Denn Software
#example file name from source >> Denn Cad-Cam. User's Manual_EN.pdf

#example file destination >> N:\Equipment_New_Sharepoint\F\FO\FO-52\MAN\
#example resulting file name after processing >> DENN-Software_Denn-Cad-Cam.-User's-Manual-EN.pdf

def main():
    fileDirectoryFolderSource = "N:\Equipment\F\FO-FORMING\FO-36 Salvagnini P2XE Panel Bender\Manual\EasyDataPDF" #this is your source directory
    fileDestination = "N:\Equipment_New_Sharepoint\F\FO\FO-36\MAN" #this is where you want files sent to
    updateNamesOfFilesInDirectory(fileDirectoryFolderSource, fileDestination) 

main()

