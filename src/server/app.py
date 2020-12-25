from flask import Flask, jsonify, request, Response
from declaracionVariables import *

import string
from random import choice

import io, time, os, json, re


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html")

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/usuarios')
def users():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from user")
    rows = cur.fetchall()
    print(rows)
    return render_template("list_usuario.html",rows = rows)

@app.route('/nuevo_parque')
def new_parque():
    return render_template("registro_parque.html")


@app.route('/lista_parques')
def list_parks():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from park")
    rows = cur.fetchall()
    print(rows)
    return render_template("list_park.html",rows = rows)

@app.route('/rest/parque/nuevo', methods=['POST'])
def POST_parqu():
    print('Peticion a /rest/parque/nuevo')
    respons = {}
    respons['ruta'] = '/rest/parque/nuevo'
    respons = jsonify(respons)

    park_dict = request.form.to_dict()
    print(park_dict)
    nombre = park_dict['nombre']
    descripcion = park_dict['descripcion']
    latitud = park_dict['latitud']
    longitud = park_dict['longitud']
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO park (nombre, descripcion, latitud, longitud) VALUES (?,?,?,?)",(nombre,descripcion,latitud,longitud) )
        con.commit()
        respons.status_code = 201
    con.close()
    return redirect("/nuevo_parque", code=201)

@app.route('/rest/usuario', methods=['POST'])
def POST_user():
    print('Peticion a /rest/usuario')
    respons = {}
    respons['ruta'] = '/rest/usuario'
    respons = jsonify(respons)
    with sql.connect("database.db") as con:
        try:
            value = request.get_json()
            
            email = value.get('email')
            password = value.get('password')
            rol = value.get('rol')
            cur = con.cursor()
            cur.execute("INSERT INTO user (email, password, rol) VALUES (?,?,?)",(email,password,rol) )
            con.commit()
            respons.status_code = 201
        except:
            print("Ya existe un usuario con ese email")
            con.close()
            respons.status_code = 400
    con.close()
    return respons

@app.route('/rest/usuario/change_password', methods=['POST'])
def change_password_user():
    print('Peticion a /rest/usuario/change_password')
    email = request.get_json()
    respons = {}
    respons['ruta'] = '/rest/usuario/change_password'
    respons = jsonify(respons)
    with sql.connect("database.db") as con:
        try:            
            cur = con.cursor()
            cur.execute("UPDATE user SET urlpassword = ? WHERE email = ?",(''.join([choice(string.ascii_letters) for i in range(10)]),email) )
            con.commit()
            respons.status_code = 201
        except:
            print("Ya existe un usuario con ese email")
            con.close()
            respons.status_code = 400
    con.close()
    return respons

@app.route('/rest/usuario/login', methods=['POST'])
def login_user():
    print('Peticion a /rest/usuario/login')
    email = request.get_json()
    respons = {}
    respons['ruta'] = '/rest/usuario/login'
    respons = jsonify(respons)
    value = request.get_json()
            
    email = value.get('email')
    password = value.get('password')

    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM user WHERE email = ? AND password = ?", (email,password))
    rows = cur.fetchall()

    print(rows)
    print(len(rows))

    result=cur.fetchone()
    number_of_rows=result[0]
    if number_of_rows == 1:
        respons.status_code = 201
    else:
        respons.status_code = 400
    return respons

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port,debug=DEBUG)