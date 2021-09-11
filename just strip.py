# -*- coding: utf-8 -*-
# Strips \n characters from each line in a txt file

import subprocess
import win32clipboard

def main():

    strip_new_line()
    #open_file()



def strip_new_line():

    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()

    no_enter = data.split()  # Splits words that are copied into a list
    no_enter2 = ''  # Creates string

    #for ele in no_enter:
        #f ele[0] = "g" and ele[-1] = "h":
            

    for ele in no_enter:  # Goes through each word that was splitted earlier
        if ele[-1] != "-" and ele[0] != "-":
            no_enter2 += ' ' + ele  # Creates new string that has proper spacing

    no_enter2 = no_enter2[1:]  # Removes space? I think


    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(no_enter2)
    win32clipboard.CloseClipboard()

def open_file():

    subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

main()
