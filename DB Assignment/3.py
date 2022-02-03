'''
3. Write a Python program to create a table and insert some records in that table. Finally selects all rows 
from the table and display the records
'''
import db
from tabulate import tabulate

conn = db.connect("assignment.db")

# creating database
db.create_table(conn, 'worker', ('worker_id integer primary key autoincrement', 'first_name varchar(20)',
                'last_name varchar(20)', 'salary float', 'joining_date date', 'department varchar(10)'))
db.create_table(conn, 'bonus', ('worker_ref_id int references worker(worker_id)',
                'bonus_date date', 'bonus_amount float'))
db.create_table(conn, 'title', ('worker_ref_id int references worker(worker_id)',
                'worker_title varchar(20)', 'affected_from date'))


db.selectAll(conn, 'worker')

# inserting rows
workers = [
    (1, 'Monika', 'Arora', 100000, '2014-02-20', 'HR'),
    (2, 'Niharika', 'Verma', 80000,  '2014-06-11', 'Admin'),
    (3, 'Vishal', 'Singhal', 300000, '2014-02-20', 'HR'),
    (4, 'Amitabh', 'Singh', 500000, '2014-02-20', 'Admin'),
    (5, 'Vivek', 'Bhati', 500000, '2014-06-11', 'Admin'),
    (6, 'Vipul', 'Diwan', 200000, '2014-06-11', 'Account'),
    (7, 'Satish', 'Kumar', 75000,  '2014-01-20', 'Account'),
    (8, 'Geetika', 'Chauhan', 90000,  '2014-04-11', 'Admin')]

bonus = [
    (1, '2016-02-20', 5000),
    (2, '2016-06-11', 3000),
    (3, '2016-02-20', 4000),
    (1, '2016-02-20', 4500),
    (2, '2016-06-11', 3500)
]

title = [
    (1, 'Manager', '2016-02-20'),
    (2, 'Executive', '2016-06-11'),
    (8, 'Executive', '2016-06-11'),
    (5, 'Manager', '2016-06-11'),
    (4, 'Asst. Manager', '2016-06-11'),
    (7, 'Executive', '2016-06-11'),
    (6, 'Lead', '2016-06-11'),
    (3, 'Lead', '2016-06-11')
]


db.insertMany(conn, 'worker', values=workers)
db.insertMany(conn, 'bonus', values=bonus)
db.insertMany(conn, 'title', values=title)


# displaying records
print(tabulate(db.selectAll(conn, 'worker'), headers=[
      "worker_id", "first_name", "last_name", "salary", "joining_date", "department"]), end="\n\n")

print(tabulate(db.selectAll(conn, 'bonus'), headers=[
      "worker_ref_id", "bonus_date", "bonus_amount"]), end="\n\n")

print(tabulate(db.selectAll(conn, 'title'), headers=[
      "worker_ref_id", "worker_title", "affected_from"]))
conn.close()
