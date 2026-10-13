from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('praktikum.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mahasiswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return "Halo dari Flask + Docker + Jenkins!"

@app.route('/mahasiswa')
def mahasiswa():
    conn = sqlite3.connect('praktikum.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM mahasiswa')
    data = cursor.fetchall()
    conn.close()

    return jsonify(data)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
