import sqlite3


def create_db():
    db = sqlite3.connect("sample.db")
    c = db.cursor()
    c.execute("create table if not exists Bank3(id integer primary key,name text,age integer,bal integer,date1 text)")
    db.commit()
