import sqlite3

"""
Connect db

"""
def create_db():
    db = sqlite3.connect("bank.db")
    c=db.cursor()
    c.execute("CREATE TABLE if not exists CUSTOMER(ID INTEGER PRIMARY KEY,Name text,Age INTEGER,Phone INTEGER,Address text)")
    c.execute("CREATE TABLE if not exists ACCOUNT(ID INTEGER PRIMARY KEY,Name text,Age INTEGER,Balance INTEGER,date1 text)")
    c.execute("CREATE TABLE if not exists DEPOSIT(ID INTEGER PRIMARY KEY,Balance INTEGER,date1 text)")
    c.execute("CREATE TABLE if not exists WITHDRAW(ID INTEGER PRIMARY KEY,WTH_Amount INTEGER,Balance INTEGER,date1 text)")
    c.execute("CREATE TABLE if not exists BANKER(ID INTEGER PRIMARY KEY,Mail,text,Name text)")
    db.commit()