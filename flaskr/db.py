import sqlite3
import click



#conn = sqlite3.connect('database.db')
#conn.execute('CREATE TABLE users (name TEXT, email TEXT, password TEXT)')
#conn.close()
def get_db(commend):
    conn = sqlite3.connect('groot_tasks.db')
    cur = conn.cursor()
    cur.execute(commend)
    rows = cur.fetchall()  
    print(rows)   
    return rows 





def insert_db(commend):
    conn = sqlite3.connect('groot_tasks.db')
    cur = conn.cursor()
    cur.execute(commend)
    conn.commit()
    conn.close()