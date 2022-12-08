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
def askInfo():
    """
    Asks the user for the start year, end year, and animal
    :return: str, int
    """
    START_YR = input("Start Year? (Starting from 1905 up to and including 2017) ")
    END_YR = input("End Year? (Starting from 1905 up to and including 2017) ")
    ANIMAL = input("Bison (1), Elk (2), Moose (3), Deer (4), or All (5)? ")
    try:
        START_YR = int(START_YR)
        END_YR = int(END_YR)
        ANIMAL = int(ANIMAL)
    except ValueError:
        print("Please enter viable values.")
        return askInfo()
    if START_YR < 1905 or START_YR > 2017 or END_YR < 1905 or END_YR > 2017:
        print("Please enter valid values")
        return askInfo()
    return START_YR, END_YR, ANIMAL
def askAdd():
    """
    Asks the user the information about the new data
    :return: list --> array
    """
    DATA = []
    AREA = (input("(North) or (South), please put proper capitalization. "))
    POPYR = (input("What is the year of the population? "))
    SURVYR = (input("What is the survey year? "))
    SURVMON = (input("What is the month of the survey? "))
    SURVDAY = (input("What is the day of the survey? "))
    SPECIES = (input("What is the name of your species? Elk, Bison, Deer, or Moose (Please input proper capitalization) "))
    AGE = input("What is the age and sex count? ")
    ADULTMALE = (input("Adult male count: "))
    ADULTFEMALE = (input("Adult female count: "))
    ADULTUNKNOWN = (input("Adult unknown count: "))
    YEARLING = (input("Yearling count: "))
    CALF = (input("Calf count: "))
    SURVTOT = (input("Survey total: "))
    SIGHTCORRECT = (input("Sightability correction: "))
    ADDITIONCAPTIVE = (input("Additional captive count: "))
    ANIMALREMOVE = (input("Animals removed prior: "))
    FALLPOP = input("Fall population: ")
    COMMENT = input("Comment: ")
    ESTIMATE = input("Estimate Method: ")
    if AREA == "North" or AREA == "South" or SPECIES == "Elk" or SPECIES == "Bison" or SPECIES == "Deer" or SPECIES == "Moose":
        if POPYR.isnumeric() and SURVYR.isnumeric() and SURVMON.isnumeric() and SURVDAY.isnumeric() and AGE.isnumeric() and ADULTMALE.isnumeric() and ADULTFEMALE.isnumeric() and ADULTUNKNOWN.isnumeric() and YEARLING.isnumeric() and CALF.isnumeric() and SURVTOT.isnumeric() and SIGHTCORRECT.isnumeric() and ADDITIONCAPTIVE.isnumeric() and ANIMALREMOVE.isnumeric() and FALLPOP.isnumeric():
            DATA.append(AREA)
            DATA.append(POPYR)
            DATA.append(SURVYR)
            DATA.append(SURVMON)
            DATA.append(SURVDAY)
            DATA.append(SPECIES)
            DATA.append(AGE)
            DATA.append(ADULTMALE)
            DATA.append(ADULTFEMALE)
            DATA.append(ADULTUNKNOWN)
            DATA.append(YEARLING)
            DATA.append(CALF)
            DATA.append(SURVTOT)
            DATA.append(SIGHTCORRECT)
            DATA.append(ADDITIONCAPTIVE)
            DATA.append(ANIMALREMOVE)
            DATA.append(FALLPOP)
            DATA.append(COMMENT)
            DATA.append(ESTIMATE)
            return DATA
        else:
            print("Enter valid values")
            return askAdd()
    else:
        print("Enter valid values")
        return askAdd()
def askViewData():
    """
    Asks the user the year and species of the animal
    :return: List --> array
    """
    YR = input("What is the year? ")
    SPECIES = input("What is the species? (Elk, Moose, Deer, Bison) ")
    try:
        YR = int(YR)
    except ValueError:
        print("Please enter a valid value.")
        return askViewData()
    if SPECIES == "Elk" or SPECIES == "Moose" or SPECIES == "Bison" or SPECIES == "Deer":
        return YR, SPECIES
    else:
        print("Enter valid values.")
        return askViewData()
# -- PROCESSING -- #
def checkBison():
    """
    :return:
    """
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
        TEXTLIST[i] = TEXTLIST[i].split('"')
        if len(TEXTLIST[i]) > 1:
            TEXTLIST[i][0] = TEXTLIST[i][0].split(',')
            TEXTLIST[i][0].pop(-1)
            COMMENT = TEXTLIST[i].pop(1)
            EXPERIMENT = TEXTLIST[i].pop(1)
            TEXTLIST[i][0].append(COMMENT)
            TEXTLIST[i][0].append(EXPERIMENT)
            TEXTLIST[i] = TEXTLIST[i][0]
            if TEXTLIST[i][-1][0] == ",":
                TEXTLIST[i][-1] = TEXTLIST[i][-1][1:]
        elif len(TEXTLIST[i]) == 1:
            for j in range(len(TEXTLIST[i])):
                TEXTLIST[i][j] = TEXTLIST[i][j].split(',')
                TEXTLIST[i] = TEXTLIST[i][0]
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
                id INTEGER PRIMARY KEY,
                area_of_park TEXT NOT NULL,
                population_year INTEGER NOT NULL,
                survey_year TEXT NOT NULL,
                survey_month TEXT NOT NULL,
                survey_day TEXT NOT NULL,
                species_name TEXT NOT NULL,
                unknown_age_sex TEXT NOT NULL,
                adult_male_count TEXT NOT NULL,
                adult_female_count TEXT NOT NULL,
                adult_unknown_count TEXT NOT NULL,
                yearling_count TEXT NOT NULL,
                calf_count TEXT NOT NULL,
                survey_total TEXT NOT NULL,
                sightability_correction TEXT NOT NULL,
                additional_captive_count TEXT NOT NULL,
                animals_removed_prior TEXT NOT NULL, 
                fall_population INTEGER,
                comment TEXT,
                estimate_method TEXT NOT NULL
                )
    ;""")
    for i in range(1, len(DATABASE)):
        CURSOR.execute("""
            INSERT INTO
                Population_data (
                    area_of_park,
                    population_year,
                    survey_year,
                    survey_month,
                    survey_day,
                    species_name,
                    unknown_age_sex,
                    adult_male_count,
                    adult_female_count,
                    adult_unknown_count,
                    yearling_count,
                    calf_count,
                    survey_total,
                    sightability_correction,
                    additional_captive_count,
                    animals_removed_prior, 
                    fall_population,
                    comment,
                    estimate_method
                    )
            VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                )
        ;""", DATABASE[i])
    CONNECTION.commit()
def findInfo(YR, SPECIES):
    """
    Finds the data the user has requested
    :param YR: int
    :param SPECIES: str
    :return: list
    """
    global CURSOR
    DATA  = CURSOR.execute("""
            SELECT
                *
            FROM
                Population_data
            WHERE
                population_year = ?
            AND 
                species_name = ?
        ;""", [YR, SPECIES])
def findValues(START_YR, END_YR, ANIMAL):
    """
    This finds the values of the start yr of the animal, the end year of the animal, and the animal chosen. If all, then there will not be a species name input, it will just get the populations of all that year.
    :param START_YR: int
    :param END_YR: int
    :param ANIMAL: int
    :return:
    """
    global CURSOR, CHOICE
    if ANIMAL < 5:
        if ANIMAL == 1:
            ANIMAL = "Bison"
        elif ANIMAL == 2:
            ANIMAL = "Elk"
        elif ANIMAL == 3:
            ANIMAL = "Moose"
        elif ANIMAL == 4:
            ANIMAL = "Deer"
        DATABEGIN = CURSOR.execute("""
            SELECT
                fall_population
            FROM 
                Population_data
            WHERE
                population_year = ?
            AND
                species_name = ?
        ;""", [START_YR, ANIMAL]).fetchall()
        DATAEND = CURSOR.execute("""
            SELECT
                fall_population
            FROM
                Population_data
            WHERE
                population_year = ?
            AND 
                species_name = ?
        ;""", [END_YR, ANIMAL]).fetchall()
        if DATABEGIN == []:
            DATABEGIN = [(0,), (0,)]
        for i in range(len(DATABEGIN)):
            DATABEGIN[i] = DATABEGIN[i][0]
        if DATABEGIN[0] == "NA":
            DATABEGIN[0] = 0
        if len(DATABEGIN) == 1:
            DATABEGIN.append(0)
        elif DATABEGIN[1] == "NA":
            DATABEGIN[1] = 0
        if DATAEND == []:
            DATAEND = [(0,), (0,)]
        for i in range(len(DATAEND)):
            DATAEND[i] = DATAEND[i][0]
        if DATAEND[0] == "NA":
            DATAEND[0] = 0
        if len(DATAEND) == 1:
            DATAEND.append(0)
        elif DATAEND[1] == "NA":
            DATAEND[1] = 0
        return DATABEGIN, DATAEND

    else:
        DATABEGIN = CURSOR.execute("""
                    SELECT
                        fall_population
                    FROM 
                        Population_data
                    WHERE
                        population_year = ?
                ;""", [START_YR]).fetchall()
        DATAEND = CURSOR.execute("""
                    SELECT
                        fall_population
                    FROM
                        Population_data
                    WHERE
                        population_year = ?
                ;""", [END_YR]).fetchall()
        for i in range(len(DATABEGIN)):
            DATABEGIN[i] = DATABEGIN[i][0]
            if DATABEGIN[i] == "NA":
                DATABEGIN[i] = 0
        for i in range(len(DATAEND)):
            DATAEND[i] = DATAEND[i][0]
            if DATAEND[i] == "NA":
                DATAEND[i] = 0
        return DATABEGIN, DATAEND
def calculateGrowthIndividual(START, END, START_YR, END_YR, ANIMAL):
    """
    Calculates the population growth for individual animals
    :param START: list
    :param END: list
    :param: START_YR: int
    :param: END_YR: int
    :param: ANIMAL: int
    :return: float
    """
    if ANIMAL < 5:
        ANSWER = ((END[0] + END[1]) - (START[0] + START[1]))/(END_YR - START_YR)
        return ANSWER
    else:
        pass
def calculateGrowthAll(START, END, START_YR, END_YR, ANIMAL):
    """
    Calculates the growth of all the animals in that population group.
    :param START: list
    :param END: list
    :param START_YR: int
    :param END_YR: int
    :param ANIMAL: int
    :return: float
    """
    if ANIMAL == 5:
        ANSWER = (sum(END)-sum(START))/(END_YR - START_YR)
        return ANSWER
    else:
        pass
def addNewRow(DATA):
    """
    Adds the data from the returned values of the list into the sqlite table
    :param DATA: list
    :return: none
    """
    global CURSOR, CONNECTION
    CURSOR.execute("""
        INSERT INTO
            Population_data (
                    area_of_park,
                    population_year,
                    survey_year,
                    survey_month,
                    survey_day,
                    species_name,
                    unknown_age_sex,
                    adult_male_count,
                    adult_female_count,
                    adult_unknown_count,
                    yearling_count,
                    calf_count,
                    survey_total,
                    sightability_correction,
                    additional_captive_count,
                    animals_removed_prior, 
                    fall_population,
                    comment,
                    estimate_method
                    )
        VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
    ;""", DATA)
    CONNECTION.commit()
# -- OUTPUTS -- #
def displayGrowth(ANSWER, ANSWER_2, START, END, ANIMAL):
    """
    Displays the answer of the search population growth
    :param ANSWER: float
    :return: none
    """
    if ANIMAL < 5:
        if ANIMAL == 1:
            ANIMAL = "Bison"
        elif ANIMAL == 2:
            ANIMAL = "Elk"
        elif ANIMAL == 3:
            ANIMAL = "Moose"
        elif ANIMAL == 4:
            ANIMAL = "Deer"
        print(f"The growth rate of {ANIMAL} between {START} and {END} is {ANSWER} {ANIMAL}/year.")
    else:
        print(f"The growth rate of all animals between {START} and {END} is {ANSWER_2} animals/year.")
# --- VARIABLE --- #
DATAFILE = "Population.db"

FIRST_RUN = True

if (pathlib.Path.cwd() / DATAFILE).exists():
    FIRST_RUN = False
CONNECTION = sqlite3.connect(DATAFILE)
CURSOR = CONNECTION.cursor()

# ------ MAIN PROGRAM CODE ------ #
if __name__ == "__main__":
    if FIRST_RUN:
        DATABASE = setup("Elk_Island_NP_Grassland_Forest_Ungulate_Population_1906-2017_data_reg.txt")
        setupAll(DATABASE)
    # --- INPUTS --- #
    CHOICE = askChoice()
    if CHOICE == 1:
        # --- INPUTS
        START_YR, END_YR, ANIMAL = askInfo()
        # --- PROCESSING --- #
        STARTPOP, ENDPOP = findValues(START_YR, END_YR, ANIMAL)
        ANSWER = calculateGrowthIndividual(STARTPOP, ENDPOP, START_YR, END_YR, ANIMAL)
        ANSWER_2 = calculateGrowthAll(STARTPOP, ENDPOP, START_YR, END_YR, ANIMAL)
        # --- OUTPUTS --- #
        displayGrowth(ANSWER,ANSWER_2, START_YR, END_YR, ANIMAL)
    if CHOICE == 2:
        # --- INPUTS --- #
        DATA = askAdd()
        # --- PROCESSING --- #
        addNewRow(DATA)
        # --- OUTPUT --- #
        print("Data successfully added!")
    if CHOICE == 3:
        YR, SPECIES = askViewData()





