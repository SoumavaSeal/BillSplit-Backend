from flask import Blueprint, jsonify, request
from config import connect

dataEntry = Blueprint("dataEntry", _name_, url_prefix="/")

@dataEntry.post('/userentry')
def userentry():
    content = request.get_json()
    name = content['name']
    username = content['uname']
    conn = connect()
    cur = conn.cursor()
    cur.execute("insert into users (name, username) values('" + name + "', '" + username + "');")
    conn.commit()
    cur.close()
    conn.close()
    return {"Status":"User added Successfully"}

@dataEntry.post('/groupentry')
def groupentry():
    content = request.get_json()
    grp_name = content[ 'gname']
    conn = connect()
    cur = conn.cursor()
    cur.execute("insert into groups (grp_name) values ('" + grp_name +"');")
    conn.commit()
    cur.close()
    conn.close()
    return{"status":"group added succesfully"}


@dataEntry.post('/billentry')
def billentry():
    content = request.get_json()
    tilte = content['btitle']
    amount = content['bamount']
    type = content['btype']
    location = content['bloc']
    grp_id = content['grp_id']
    bill_id = content['bill_id']
    share = content['share']
    conn = connect()
    cur = conn.cursor()
    cur.execute("insert into bills (title,amount,type,location,grp_id) values ('" + tilte + "' , '" + amount + "' , '" + type + "' , '" + location + "' , '" + grp_id + "'); ")
    
    for i in share:
        cur.execute("insert into transactions (user_id, bill_id, share_val) values ({0}, {1}, {2})".format(i, bill_id, share[i]))

    conn.commit()
    cur.close()
    conn.close()
    return{"status":"bills added succesfully"}