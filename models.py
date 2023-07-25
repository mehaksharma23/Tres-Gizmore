import sqlite3

def insertToken(token):
    conn = sqlite3.connect('instance/database.db')
    command = "INSERT INTO access_token (token) VALUES ('{token}')"
    conn.execute("INSERT INTO access_token (token) \
      VALUES ('{token}')")
    conn.commit()
    conn.close()
