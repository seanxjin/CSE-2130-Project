'''
title: Large Mammal Populations Elk Island National Park
author: Sean Jin
date-created: 2022-11-25
'''

import pathlib
import sqlite3

# --- SUBROUNTINE --- #

# -- INPUT -- #
def askChoice():
    """
    Asks the user for their choice of calculation
    :return: int
    """
    print("""Welcome to the Elk Island National Park Large Mammal population database!
Please choose an option:
    1. Search Population Growth
    2. Add New Year Data
    3. Delete Data
    4. Exit
    """)
    CHOICE = input("> ")
    try:
        CHOICE = int(CHOICE)
    except ValueError:
        print("Please enter a possible integer!")
        return askChoice()
    if CHOICE > 0 and CHOICE < 5:
        pass
    else:
        print("Please enter a possible value!")
        return askChoice()
    return CHOICE
# -- PROCESSING -- #
def setup(FILENAME):
    """
    Opens the file and extracts the contents of the file, joins the commas in the comments
    :param: str
    :return: list -- > 2d array
    """
    FILE = open(FILENAME)
    TEXTLIST = FILE.readlines()
    FILE.close()
    for i in range(len(TEXTLIST)):
        if TEXTLIST[i][-1] == "\n":
            TEXTLIST[i] = TEXTLIST[i][:-1]
        TEXTLIST[i] = TEXTLIST[i].split(',')
        while len(TEXTLIST[i]) > 19:
            TEXTLIST[i][17] = ",".join([TEXTLIST[i][j] for j in [17, 18]])
            TEXTLIST[i].pop(18)
        for j in range(len(TEXTLIST[i])):
            if TEXTLIST[i][j].isnumeric():
                TEXTLIST[i][j] = int(TEXTLIST[i][j])
    return TEXTLIST
def setupAll(DATABASE):
    """
    Creates a table using the separated database
    :param DATABASE: list --> 2d array
    :return: none
    """
    global CURSOR, CONNECTION
    CURSOR.execute("""
        CREATE TABLE
            Population_data (
                id INTEGER PRIMARY KEY
                area_of_park TEXT NOT NULL,
                population_year INTEGER NOT NULL,
                survey_year INTEGER
                survey_month INTEGER,
                survey_day INTEGER,
                species_name TEXT NOT NULL,
                unknown_age_sex INTEGER,
                adult_male_count INTEGER,
                adult_female_count INTEGER,
                adult_unknown_count INTEGER,
                yearling_count INTEGER,
                calf_count INTEGER,
                survey_total INTEGER,
                sightability_coor
                
    ;""")
# -- OUTPUTS -- #

# --- VARIABLE --- #
DATAFILE = "Population.db"

FIRST_RUN = True

if (pathlib.Path.cwd() / DATAFILE).exists():
    FIRST_RUN = False
CONNECTION = sqlite3.connect(DATAFILE)
CURSOR = CONNECTION.cursor()

if __name__ == "__main__":
    if FIRST_RUN:
        DATABASE = print(setup("Elk_Island_NP_Grassland_Forest_Ungulate_Population_1906-2017_data_reg.txt"))
        setupAll(DATABASE)
    CHOICE = askChoice()
    if CHOICE == 1:



