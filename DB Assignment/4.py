'''4. Write a Python program to perform CURD operation into a given SQLite table.'''

import db
from tabulate import tabulate

conn = db.connect("assignment.db")

# CREATE OPERATION
print("CREATE OPERATION\n")
db.create_table(conn, 'student', columns=(
    'stud_id integer primary key autoincrement', 'stud_name varchar(30)', 'class varchar(10)'))

# INSERTs
students = [('Shubham', 'MCS - 1'), 
            ("Wallabh", "MCA - 1"),
            ("Yash", "MCs - 1"), 
            ("Iron Man", "MTech")]

db.insertMany(conn, 'student', columns=('stud_name', 'class'), values=students)

# READ OPERATION
print("READ OPERATION\n")

result = db.selectAll(conn, 'student')
print(tabulate(result),end="\n\n\n")

result = db.selectAll(conn, 'student', 'stud_name = "Shubham"')
print(tabulate(result), end="\n\n\n")

#UPDATE OPERATION
print("UPDATE OPERATION\n")

db.update(conn, 'student', 'class', 'BTech', 'stud_name = "Iron Man"')
result = db.selectAll(conn, 'student')
print(tabulate(result), end="\n\n\n")

#DELETE OPERATION
print("DELETE OPERATION\n")

db.delete(conn, 'student', 'stud_name = "Iron Man"')
result = db.selectAll(conn, 'student')
print(tabulate(result), end="\n\n\n")