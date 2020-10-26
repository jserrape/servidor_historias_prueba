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
    print('Peticion a /rest/usuario')
    print(request.headers)
    print('------------------------')
    print(request.get_json())
    value = request.get_json()
    print(value.get('title'))

    print('------------------------')
    print(request.args)
    print('------------------------')
    print(request.form)
    print('------------------------')
    return 'ok'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port,debug=DEBUG)