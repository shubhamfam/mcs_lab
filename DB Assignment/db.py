import sqlite3
from sqlite3 import Error


def connect(db):
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error:
        print(Error)


def create_table(conn, table, columns=()):
    if not columns:
        raise Exception('Please provide columns')
    try:
        cursor = conn.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {table}")
        sql = ("create table " + table + str(columns)).replace("'", "")
        cursor.execute(sql)
        print(f"{table} table created successfully.")
        conn.commit()
    except Error:
        print(Error)


def insertOne(conn, table, values=(), columns=()):
    try:
        cursor = conn.cursor()
        columns = str(columns) if columns else ""
        sql = "insert into " + table + columns + " values " + str(values)
        cursor.execute(sql)
        print(f"Data inserted successfully.")
        conn.commit()
    except Error:
        print(Error)


def insertMany(conn, table, columns=(), values=()):
    try:
        cursor = conn.cursor()
        columns = str(columns) if columns else ""
        holders = ("?," * len(values[0]))[:-1]
        sql = "insert into " + table + columns + " values(" + holders + ")"
        cursor.executemany(sql, values)
        print(f"Data inserted successfully.")
        conn.commit()
    except Error:
        print(Error)


def selectAll(conn, table, condition=""):
    sql = (f"select * from {table} where {condition}") if condition else f"select * from {table}"
    print(sql)
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        conn.commit()
        return result
    except Error:
        print(Error)


def update(conn, table, column, value, condition=""):
    value = f"\'{value}\'" if isinstance(value, str) else str(value)

    sql = f"update {table} set {column} = {value}" + (" where "+condition if condition else "") 
    print(sql)


conn = connect("assignment.db")

update(conn, "assi", "status", False)