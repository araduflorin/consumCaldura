#from consumCald import app
import sqlite3
from datetime import datetime
#from unittest import result
from flask import render_template, Flask, redirect, request, g


app = Flask(__name__)

def connect_db():
    sql = sqlite3.connect('consumCald/consumCald.db')
    #sql = sqlite3.connect('postgres://wduimatuuahmwd:897800e58cb3e509742e92b6d8335765c74a4f684f495e68cfd37d786fb4c4c3@ec2-3-223-213-207.compute-1.amazonaws.com:5432/dd9g3omh3iiil7')
    sql.row_factory = sqlite3.Row
    return sql


def get_db():
    #Check if DB is there
    if not hasattr(g, 'sqlite3'):
        g.sqlite3_db = connect_db()
    return g.sqlite3_db

@app.route('/')
def home():
    db=get_db()
    cursor=db.execute("SELECT * FROM consumCald")
    result=cursor.fetchall()
    return render_template('home.html', inreg=result)

@app.route("/adaugaCald", methods=['GET','POST'])
def adaugaCald():
    if request.method == "POST":
        sufragerie = request.form['sufragerie']
        bucatarie = request.form["bucatarie"]
        dormitorMic = request.form["dormitorMic"]
        dormitorMare = request.form["dormitorMare"]
        baie = request.form["baie"]
        wc = request.form["wc"]
        #data = datetime.utcnow
        data = datetime.now()
        format_data = data.strftime('%d.%m.%Y %H:%M')
        #tipApa = "rece"
        db=get_db()
        cursor = db.execute("INSERT INTO consumCald (Sufragerie, Bucatarie, DormitorMic, DormitorMare, Baie, WC, Data) VALUES(?, ?, ?, ?, ?, ?, ?)", (sufragerie, bucatarie, dormitorMic, dormitorMare, baie, wc, format_data))
        
        db.commit()
        return redirect('/')    

@app.route("/modificaCald", methods=['GET','POST'])
def modificaCald():
    if request.method == "POST":
        sufragerie = request.form['sufragerie']
        bucatarie = request.form["bucatarie"]
        dormitorMic = request.form["dormitorMic"]
        dormitorMare = request.form["dormitorMare"]
        baie = request.form["baie"]
        wc = request.form["wc"]
        id = request.form['id']
        #data = datetime.utcnow
        data = datetime.now()
        format_data = data.strftime('%d.%m.%Y %H:%M')

        db=get_db()        
        cursor = db.execute("""UPDATE consumCald SET Sufragerie=?, Bucatarie=?, DormitorMic=?, DormitorMare=?, Baie=?, WC=?, Data=? WHERE id=?;""", (sufragerie, bucatarie, dormitorMic, dormitorMare, baie, wc, format_data, id))
        
        db.commit()
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)