import sqlite3 as sql
from flask import current_app, g
from flask.cli import with_appcontext

def get_db(commend):
    conn = sql.connect('groot_tasks.db')
    cur = conn.cursor()
    cur.execute(commend)
    rows = cur.fetchall()  
    return rows





def insert_db(commend):
    conn = sql.connect('groot_tasks.db')
    cur = conn.cursor()
    cur.execute(commend)
    conn.commit()
    conn.close()

