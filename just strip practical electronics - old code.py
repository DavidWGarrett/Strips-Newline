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


    prev_chara = " "
    data2 = ''


    # This for loop attempts to deal with hyphens at the end of each new line. I figured out how
    # to deal with the extra space, but not the hyphen between new lines ex (elec-tricity)
    # as far as I can tell, this for loop does nothing
    for chara in data:

        if chara == ' ' and prev_chara == '-':
            data2 += prev_chara
        elif chara == '\n':
            pass
        elif chara != '-':
            data2 += chara

        prev_chara = chara

    print(data2)

    #print(data2)


    no_enter = data2.split()  # Splits words that are copied into a list
    no_enter2 = ''  # Creates string

    #for ele in no_enter:
        #f ele[0] = "g" and ele[-1] = "h":

    prev_ele = 'a'  # Stores previous element for the for loop below.
    #print(no_enter)

    for ele in no_enter:  # Goes through each word that was splitted earlier
        # Attempts to to deal with the problem when a hyphen gets copied from the pdf file,
        # There's an extra space after each hyphen.
        if prev_ele[-1] == "-":
            no_enter2 += ele
        else: 
            no_enter2 += ' ' + ele  # Creates new string that has proper spacing
        prev_ele = ele

    no_enter2 = no_enter2[1:]  # Removes space? I think


    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(no_enter2)
    win32clipboard.CloseClipboard()

def open_file():

    subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

main()

