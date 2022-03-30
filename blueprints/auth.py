from flask import Blueprint, jsonify, request
from config import connect

auth = Blueprint("auth", __name__, url_prefix="/")

@auth.post('/register')
def register():
    content = request.get_json()
    username = content['uname']
    contact = content['contact']
    conn = connect()
    cur = conn.cursor()
    cur.execute("insert into users (name, contact) values('" + username + "', " + str(contact) + ");")
    conn.commit()
    cur.close()
    conn.close()
    return {"Status":"Success"}

@auth.get('/user')
def query():
    content = request.get_json()
    username = content['uname']
    conn = connect()
    cur = conn.cursor()
    query = "select * from users where name='" + username + "';"
    cur.execute(query)
    a = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(a);


