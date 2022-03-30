import re
from unittest import result
from flask import Blueprint, jsonify, request
from config import connect

users = Blueprint("userDetails", __name__, url_prefix="/")

@users.get('/usrInGrp')
def usrInGrp():
    content = request.get_json()
    grpName = content['grpName']
    conn = connect()
    cur = conn.cursor()
    cur.execute("select distinct u.id,u.name from users u,transactions t,bills b,groups g where u.id=t.user_id and t.bill_id=b.bill_id and b.grp_id=g.grp_id and g.grp_name='{0}' order by u.id;".format(grpName))
    result = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(result)

@users.get('/groupsForUser')
def grpForUser():
    content = request.get_json()
    username = content['uname']
    conn = connect()
    cur = conn.cursor()
    query = "select distinct g.grp_name from users u,transactions t,bills b,groups g where u.id=t.user_id and t.bill_id=b.bill_id and b.grp_id=g.grp_id and u.name='{0}';".format(username)
    cur.execute(query)
    a = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(a);

@users.get('/usrInBill')
def usrInBill():
    content = request.get_json()
    grpName = content['grpName']
    billId = content['billId']
    conn = connect()
    cur = conn.cursor()
    query = "select distinct u.id, u.name from users u,transactions t,bills b,groups g where u.id=t.user_id and t.bill_id=b.bill_id and b.grp_id=g.grp_id and g.grp_name='{0}' and b.bill_id={1} order by u.id;".format(grpName, billId)
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(result);

@users.get('/usrShareInGrp')
def usrShareInGrp():
    content = request.get_json()
    grpId = content['grpId']
    conn = connect()
    cur = conn.cursor()
    q1 = "select distinct u.id,u.name from users u,transactions t,bills b,groups g where u.id=t.user_id and t.bill_id=b.bill_id and b.grp_id=g.grp_id and g.grp_id='{0}' order by u.id;".format(grpId)
    cur.execute(q1)
    r1 = cur.fetchall()
    result = []
    for i in r1:
        usrId = i[0]
        usrName = i[1]
        q2 = "select sum(t.share_val) sum from users u,transactions t,bills b,groups g where u.id=t.user_id and t.bill_id=b.bill_id and b.grp_id=g.grp_id and u.id='{0}' and g.grp_id='{1}'; ".format(usrId, grpId)
        cur.execute(q2)
        temp = cur.fetchone()
        result.append([usrId, usrName, temp[0]])

    return jsonify(result)


