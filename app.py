# app.py
from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

def query_db(query, args=(), one=False):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    conn.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/')
def home():
    return '''
    <h1>Login</h1>
    <form method="POST" action="/login">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    result = query_db(query)
    if result:
        return f"Welcome {username}!"
    else:
        return "Login failed."

@app.route('/logs')
def logs():
    auth = request.authorization
    if auth and auth.username == 'admin' and auth.password == 'securepass':
        with open('server_logs.txt', 'r') as file:
            logs = file.read()
        return f"<pre>{logs}</pre>"
    return 'Unauthorized', 401

if __name__ == '__main__':
    app.run(debug=True)
