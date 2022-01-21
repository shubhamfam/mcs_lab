'''2.Write a Python program to insert a list of records into a given SQLite table.'''
import db
from tabulate import tabulate

#assignment table (id, name, subject, completition_status)
assignments = [
    ("RDBMS", "ADC", True),
    ("Notes on Human Rights", "Human Rights", False),
    ("Assignment 1", "AI", True),
    ("Assignment 2", "AI", True),
    ("Assignment 3", "AI", True),
    ("Database with python", "Python", False),
    ("Client-Server Notes", "ADC", True),
    ("DAA - 1", "DAA", True)
]

conn = db.connect("assignment.db")

db.create_table(conn, 'assignments', columns=('assignment_id integer primary key autoincrement',
                'name varchar(30)', 'subject varchar(30)', 'completion_status bool'))

db.insertMany(conn, 'assignments', columns=(
    'name', 'subject', 'completion_status'), values=assignments)

print(tabulate(db.selectAll(conn, 'assignments'), headers=[
      'id', 'name', 'subject', 'completion_status']))

conn.close()
