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

    no_enter = data.split()
    no_enter2 = ''

    for ele in no_enter:
        if ele[-1] != "-" and ele[0] != "-":
            no_enter2 += ' ' + ele

    no_enter2 = '(C) ' + no_enter2[1:]

    no_enter2 = no_enter2.replace(" ,", ",")
    no_enter2 = no_enter2.replace('``', '"')
    no_enter2 = no_enter2.replace(" .", ".")


    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(no_enter2)
    win32clipboard.CloseClipboard()

def open_file():

    subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

main()
