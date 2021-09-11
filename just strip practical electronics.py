# -*- coding: utf-8 -*-
# Strips \n characters from each line in a txt file

import subprocess
import win32clipboard
import pyperclip

def main():

    strip_new_line()
    #open_file()



def strip_new_line():

    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()


    prev_chara = " "
    data2 = ''

    datarev4 = data.splitlines()


    for split_line in datarev4:
        if split_line[-1] == "-":
            split_line_mod = split_line[0:len(split_line)-1]
            data2 += split_line_mod
        else:
            data2 += split_line + " "


    no_enter2 = data2.replace("- ", "-")
    no_enter2 = no_enter2.replace(" ,", ",")
    no_enter2 = no_enter2.replace('``', '"')
    no_enter2 = no_enter2.replace(" .", ".")

    pyperclip.copy(no_enter2)

def open_file():

    subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

main()

