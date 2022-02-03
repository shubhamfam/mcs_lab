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
        sql = (f"create table {table} {str(columns)}").replace("'", "")
        print(sql)
        cursor.execute(sql)
        print(f"{table} table created successfully.")
        conn.commit()
    except Error:
        print(Error)


def insertOne(conn, table, values=(), columns=()):
    try:
        cursor = conn.cursor()
        columns = str(columns) if columns else ""
        sql = f"insert into {table} {columns} values {str(values)}" 
        print(sql)
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
        sql = f"insert into {table} {columns} values ({holders})"
        print(sql)
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
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    except Error:
        print(Error)

def delete(conn, table, condition=""):
    sql = f"delete from {table}" + (" where "+condition if condition else "") 
    print(sql)
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    except Error:
        print(Error)

