import sqlite3
import pandas as pd
import re

def clear_tags(value):
    return re.sub(r'<[^>]*>', '', str(value))

def main():
    con = sqlite3.connect('works.sqlite')
    cursor = con.cursor()
    cursor.execute('DROP TABLE IF EXISTS works')
    cursor.execute('CREATE TABLE works ('
                   'ID INTEGER PRIMARY KEY AUTOINCREMENT,'
                   'salary INTEGER,'
                   'educationType TEXT,'
                   'jobTitle TEXT,'
                   'qualification TEXT,'
                   'gender TEXT,'
                   'dateModify TEXT,'
                   'skills TEXT,'
                   'otherInfo TEXT)')

    data = pd.read_csv("works.csv")
    data.to_sql("works", con, if_exists='append', index=False)
    con.commit()

    # Таблица с гендерами
    cursor.execute('DROP TABLE IF EXISTS genders')
    cursor.execute('CREATE TABLE genders(gender TEXT PRIMARY KEY )')
    cursor.execute('INSERT INTO genders SELECT DISTINCT gender FROM works WHERE gender IS NOT NULL')
    con.commit()
    print(cursor.execute('SELECT * FROM genders').fetchall())
    print()

    # Таблица с образованиями
    cursor.execute('DROP TABLE IF EXISTS educations')
    cursor.execute('CREATE TABLE educations(educationType TEXT PRIMARY KEY )')
    cursor.execute('INSERT INTO educations SELECT DISTINCT educationType FROM works WHERE works.educationType IS NOT NULL')
    con.commit()
    print(cursor.execute('SELECT * FROM educations').fetchall())
    print()

    # Таблица с названиями работы
    cursor.execute('DROP TABLE IF EXISTS jobTitles')
    cursor.execute('CREATE TABLE jobTitles(jobTitle TEXT PRIMARY KEY )')
    cursor.execute('INSERT INTO jobTitles SELECT DISTINCT jobTitle FROM works WHERE jobTitle IS NOT NULL')
    con.commit()
    print(cursor.execute('SELECT * FROM jobTitles').fetchall())
    print()

    # Таблица с квалификациями
    cursor.execute('DROP TABLE IF EXISTS qualifications')
    cursor.execute('CREATE TABLE qualifications(qualification TEXT PRIMARY KEY )')
    cursor.execute('INSERT INTO qualifications SELECT DISTINCT qualification FROM works WHERE qualification IS NOT NULL')
    con.commit()
    print(cursor.execute('SELECT * FROM qualifications').fetchall())
    print()


if __name__ == '__main__':
    main()