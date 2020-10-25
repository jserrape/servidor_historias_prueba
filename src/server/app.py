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

@app.route('/rest/usuario', methods=['GET','POST'])
def POST_user():
    print('Peticion a /rest/usuario')
    print(request.headers)
    print('------------------------')
    #Insert user
    email = request.form["email"]
    password = request.form["password"]
    rol = request.form["rol"]

    #print(request.headers)
    #print(request.__dict__)

    print('-----')
    print(email)
    print(password)
    print(rol)
    print('------')

    with sql.connect("database.db") as con:
        try:
            cur = con.cursor()
            cur.execute("INSERT INTO user (email, password, rol) VALUES (?,?,?)",(email,password,rol) )
            con.commit()
        except:
            print("Ya existe un usuario con ese email")
            con.close()
            return redirect("/usuarios", code=400)
    con.close()
    return redirect("/usuarios", code=201)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port,debug=DEBUG)