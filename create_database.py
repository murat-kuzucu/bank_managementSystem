import sqlite3

"""
Connect db

"""
def create_db():
    db = sqlite3.connect("samp1.db")
    c = db.cursor()
    c.execute("create table if not exists Bank3(id integer primary key,name text,age integer,bal integer,date1 text)")
    db.commit # COMMIT command is the transactional command used to save changes invoked by a transaction to the database.