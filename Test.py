import sqlite3

FILE = "blah.db"
CONNECTION = sqlite3.connect(FILE)
CURSOR = CONNECTION.cursor()
CURSOR.execute("""
    CREATE TABLE 
        student (
            first_name TEXT,
            last_name TEXT,
            num INTEGER
            )
;""")

CURSOR.execute("""
    INSERT INTO
        student
    VALUES (
        ?, ?, ?
    )
;""",["Sean","Jin","HEHE"])
CONNECTION.commit()
CURSOR.execute("""
    INSERT INTO
        student
    VALUES (
        "Sean", "FIZ", 3
    )
;""")
CONNECTION.commit()
CURSOR.execute("""
    INSERT INTO
        student
    VALUES (
        "Sean", "HEHE", 3
    )
;""")
CONNECTION.commit()

CURSOR.execute ("""
    UPDATE
        student
    SET 
        first_name = "AJFDHIIDFNIJOSDNGOSFNGOF"
    WHERE
        first_name = "Sean"
;""").fetchall()
CONNECTION.commit()