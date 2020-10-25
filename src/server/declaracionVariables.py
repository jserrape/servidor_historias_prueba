import os

import sqlite3 as sql

from flask import Flask, redirect
from flask import render_template
from flask import jsonify
from flask import request
from flask import abort
from flask import Response

# Flask initialisation
app = Flask(__name__)
DEBUG = True

#BBDD
conn = sql.connect('database.db')
print("Opened database successfully")
# drop tables
conn.execute('DROP TABLE IF EXISTS user')
# create tables
conn.execute('CREATE TABLE IF NOT EXISTS user (email TEXT PRIMARY KEY, password TEXT, rol INTEGER)')
print("Table created successfully")
conn.close()

# insert test data
with sql.connect("database.db") as con:
    cur = con.cursor()
    cur.execute("INSERT INTO user (email, password, rol) VALUES (?,?,?)",('a@a.com','1234','0') )
    con.commit()
con.close()


# id INTEGER  AUTOINCREMENT