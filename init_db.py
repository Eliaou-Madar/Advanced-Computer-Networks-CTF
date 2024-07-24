# init_db.py
import sqlite3

def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    c.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin')")
    c.execute("INSERT INTO users (username, password) VALUES ('user', 'password')")
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
