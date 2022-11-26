'''
title: Large Mammal Populations Elk Island National Park
author: Sean Jin
date-created: 2022-11-25
'''

import pathlib
import sqlite3

# --- SUBROUNTINE --- #

# -- INPUT -- #
def setup(FILENAME):
    """
    Opens the file and extracts the contents of the file
    :param: str
    :return: list -- > 2d array
    """
    FILE = open(FILENAME)
    TEXTLIST = FILE.readlines()
    FILE.close()
    for i in range(len(TEXTLIST)):
        if TEXTLIST[i][-1] == "\n":
            TEXTLIST[i] = TEXTLIST[i][:-1]
        TEXTLIST[i]= TEXTLIST[i].split(',')
        for j in range(len(TEXTLIST[i])):
            if TEXTLIST[i][j].isnumeric():
                TEXTLIST[i][j] = int(TEXTLIST[i][j])
    return TEXTLIST

# -- PROCESSING -- #

# -- OUTPUTS -- #

# --- VARIABLE --- #
FILENAME = ""

if __name__ == "__main__":
    print(setup("Elk_Island_NP_Grassland_Forest_Ungulate_Population_1906-2017_data_reg.txt"))
