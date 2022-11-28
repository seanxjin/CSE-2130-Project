'''
title: Large Mammal Populations Elk Island National Park
author: Sean Jin
date-created: 2022-11-25
'''

import pathlib
import sqlite3

# --- SUBROUNTINE --- #

# -- INPUT -- #


# -- PROCESSING -- #
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
        if len(TEXTLIST[i]) > 19:
            TEXTLIST[i] = " ".join(TEXTLIST[i])
        for j in range(len(TEXTLIST[i])):
            if TEXTLIST[i][j].isnumeric():
                TEXTLIST[i][j] = int(TEXTLIST[i][j])
    return TEXTLIST
def joinComments(TEXTLIST):
    """
    Joins the places where the comments are supposed to be joined, but instead they are separated by commas
    :param TEXTLIST: list --> 2d array
    :return: 2d array
    """
    for i in range(len(TEXTLIST)):
        while len(TEXTLIST[i]) > 19:
            TEXTLIST[i] = " ".join(TEXTLIST[i])

# -- OUTPUTS -- #

# --- VARIABLE --- #
DATAFILE = "Population.db"

FIRST_RUN = True

if (pathlib.Path.cwd() / DATAFILE).exists():
    FIRST_RUN = False
CONNECTION = sqlite3.connect(DATAFILE)
CURSOR = CONNECTION.cursor()

if __name__ == "__main__":
    TEXTLIST = print(setup("Elk_Island_NP_Grassland_Forest_Ungulate_Population_1906-2017_data_reg.txt"))

