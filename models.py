import sqlite3

def insertToken(token):
    conn = sqlite3.connect('database.db')
    conn.execute("INSERT INTO AccessToken (id,token) \
      VALUES (1, '{token}'")
    conn.commit()
    conn.close()
