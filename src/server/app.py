from flask import Flask, jsonify, request, Response
from declaracionVariables import *

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
    return render_template("registro_usuario.html",rows = rows)

@app.route('/rest/usuario', methods=['POST'])
def POST_user():
    #Insert user
    email = request.form["email"]
    password = request.form["password"]
    rol = request.form["rol"]
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO user (email, password, rol) VALUES (?,?,?)",(email,password,rol) )
        con.commit()
    con.close()
    return redirect("/usuarios", code=201)

@app.route('/phone/usuario', methods=['POST'])
def POST_user_phone():
    print(POST_user_phone)
    print(request)
    print(request).form
    #Insert user
    email = request.form["email"]
    password = request.form["password"]
    rol = request.form["rol"]
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO user (email, password, rol) VALUES (?,?,?)",(email,password,rol) )
        con.commit()
    con.close()
    return redirect("/usuarios", code=201)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port,debug=DEBUG)