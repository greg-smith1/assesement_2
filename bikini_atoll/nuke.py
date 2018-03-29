#!/usr/bin/env python3

import os

def nuke():
    choice = input("do you really wish to nuke this file? (y/n)  ")
    if choice == 'y':
        os.system('zip complex_sav.zip complex')
        os.system('rm -rf complex')
        os.system('unzip complex.zip')
        os.system('zip -r complex.zip complex')
        print("-----------------------------")
        print("-----------------------------")
        print("----Bomb has been dropped----")
        print("-----------------------------")
        print("-----------------------------")

    else:
        print("Launch aborted")

nuke()
