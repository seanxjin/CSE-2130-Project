def setup(FILENAME):
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
    return TEXTLIST

print(setup("Elk_Island_NP_Grassland_Forest_Ungulate_Population_1906-2017_data_reg.txt"))