import sqlite3
import random
connection = sqlite3.connect('database_students.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS students(name integer,department,year,mark1,mark2,mark3,PRIMARY KEY (id))')
for i in range(10):
    my_student = (['max','andrew','grisha'][random.randint(2,5)],['IT','MED'][random.randint(2)],random.randint(2,5),random.randint(2,5),random.randint(2,5))
    cursor.execute('INSERT INTO students (name,department,year,mark1,mark2,mark3)VALUES(?,?,?,?,?,?)',my_student)
select_students = 'select * from students'
cursor.execute(select_students)
students = cursor.fetchall()
print('Table:\n')

for student in students:
    print(student)