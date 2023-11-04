from flask import Flask, redirect, url_for, render_template, request, session
import sqlite3

app = Flask(__name__)




@app.route("/")
def home():
    return render_template("index.html")    

@app.route("/input", methods=["POST", "GET"])
def input():
    if request.method == "POST":  
        con = sqlite3.connect("test.db")
        cur = con.cursor() 
        inp = request.args["input"]
        pri = request.args["prioritet"]
        cur.execute("Insert into test ('user','prioritet') values (?,?)",[inp,pri])
        con.commit()
        return render_template("login.html")

    elif request.method == "GET":
        con = sqlite3.connect("test.db")
        cur = con.cursor() 
        data = cur.execute("Select * from test").fetchall()
        con.commit()    
        return render_template("login.html",data=data)
        

    
@app.route("/input/<id>", methods = ["DELETE"])
def delete(id):
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    print(id)
    cur.execute("Delete from test where id = ?",[id])
    con.commit()
    return render_template("login.html")
@app.route("/input/filter/<filter>", methods = ["GET"])
def prioritet(filter):
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    if filter == "sve":
        return redirect(url_for("input"))
        

    data = cur.execute("Select * from test where prioritet = ?",[filter]).fetchall()
    con.commit()
    return render_template("login.html",data=data)

@app.route("/input/sortiranje/<sortiranje>", methods = ["GET"])
def sortiranje(sortiranje):
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    if sortiranje == "rastuci":
        data = cur.execute("Select * from test Order by prioritet asc").fetchall()
        con.commit()
        return render_template("login.html",data=data)
    elif sortiranje == "opadajuci":
        data = cur.execute("Select * from test Order by prioritet desc").fetchall()
        con.commit()
        return render_template("login.html",data=data)
        

if __name__ == "__main__":
    app.run(debug=True)   