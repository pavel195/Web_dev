import sqlite3
import random
from sqlite3 import Error
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successfull")
    except Error as e :
        print(f'error {e} has occured')
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.executemany(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.executemany(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")




def main():
    connection = create_connection('database_students')

    create_students_table = '''
    CREATE TABLE IF NOT EXISTS students(
        student_id integer primary key autoincrement,
        name text not nul ,
        department text not null,
        year integer,
        mark1 integer not null,
        mark2 integer not null,
        mark3 integer not null
    );
    '''
    execute_query(connection , create_students_table)
    marks = [int(x) for x in range(2,6)]
    names = 'alex alexander nastya kiril dasha pavel tatyana'.split()
    departments = 'IT MED PHYSICS'.split()
    years = [2022,2023]
    create_students = """INSERT INTO students (name,department,year,mark1,mark2,mark3)VALUES(?,?,?,?,?,?)',student_list"""
    execute_query(connection,create_students)
    for i in range(10):
        create_students = f"INSERT INTO students (name,department,year,mark1,mark2,mark3)VALUES({names[random.randint(len(names))]},{departments[random.randint(len(departments))]},{years[random.randint(len(years))]},{random.randint(1,6)},{random.randint(1,6)},{random.randint(1,6)};"
        execute_query(connection,create_students)
    select_students = 'select * from students'
    students = execute_read_query(connection,select_students)
    print('таблица студентов:\n')
    for student in students:
        print(student)
    connection.commit()
    connection.close()





