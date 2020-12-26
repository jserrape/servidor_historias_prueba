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
conn.execute('DROP TABLE IF EXISTS park')

# create tables
conn.execute('CREATE TABLE IF NOT EXISTS user (email TEXT PRIMARY KEY, nombre TEXT, password TEXT, rol INTEGER, urlpassword TEXT)')
conn.execute('CREATE TABLE IF NOT EXISTS park (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, descripcion TEXT, latitud TEXT, longitud TEXT)')
print("Table created successfully")
conn.close()

# insert test data
with sql.connect("database.db") as con:
    cur = con.cursor()
    cur.execute("INSERT INTO user (email, nombre, password, rol) VALUES (?,?,?,?)",('a@a.com','Juan Carlos Serrano','1234','0') )

    cur.execute("INSERT INTO park (nombre, descripcion, latitud, longitud) VALUES (?,?,?,?)",('Rotonda de la Alcantarilla','Soy la descripcion','37.762261','-3.788986') )
    cur.execute("INSERT INTO park (nombre, descripcion, latitud, longitud) VALUES (?,?,?,?)",('Gámez Mellado "Aves y Huevos"','Soy la descripcion','37.76013131070424','-3.791822653210403') )
    cur.execute("INSERT INTO park (nombre, descripcion, latitud, longitud) VALUES (?,?,?,?)",('Calle Cuesta del Molinillo','Soy la descripcion','37.76083480746699','-3.788675214870949') )
    cur.execute("INSERT INTO park (nombre, descripcion, latitud, longitud) VALUES (?,?,?,?)",('Conservatorio Profesional de Música','Soy la descripcion','37.76575909745259','-3.7922840578040393') )
    cur.execute("INSERT INTO park (nombre, descripcion, latitud, longitud) VALUES (?,?,?,?)",('Diputación Provincial de Jaén','Soy la descripcion','37.766254113619325','-3.789199524072643') )
    cur.execute("INSERT INTO park (nombre, descripcion, latitud, longitud) VALUES (?,?,?,?)",('Calle Agustina de Aragón','Soy la descripcion','37.765785150856445','-3.779856081421258') )
    cur.execute("INSERT INTO park (nombre, descripcion, latitud, longitud) VALUES (?,?,?,?)",('Fuente Nueva','Soy la descripcion','37.76508290472222','-3.7925870689570615') )
    cur.execute("INSERT INTO park (nombre, descripcion, latitud, longitud) VALUES (?,?,?,?)",('Plaza de toros de Jaén','Soy la descripcion','37.768105085538636','-3.783507286040674') )
    cur.execute("INSERT INTO park (nombre, descripcion, latitud, longitud) VALUES (?,?,?,?)",('Calle Reventón','Soy la descripcion','37.76982454702663','-3.794136070049973') )
    cur.execute("INSERT INTO park (nombre, descripcion, latitud, longitud) VALUES (?,?,?,?)",('Estanque de los Patos','Soy la descripcion','37.7726381251192','-3.7875940123019234') )
    con.commit()
con.close()


