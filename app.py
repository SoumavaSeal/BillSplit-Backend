from flask import Flask, request
from config import connect
from blueprints.auth import auth
from blueprints.userDetails import users
from blueprints.dataEntry import dataEntry

app = Flask(__name__)

app.register_blueprint(auth)
app.register_blueprint(users)
app.register_blueprint(dataEntry)

@app.route("/", methods=['GET'])
def get():
    conn = connect()
    cur = conn.cursor()
    cur.execute("select * from test;")
    a = cur.fetchall()
    # cur.execute("insert into test values(1, 'now');")
    conn.commit()
    cur.close()
    conn.close()
    return {"msg":len(a)}


if __name__ == "__main__":
    app.run(debug=True)