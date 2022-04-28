#from consumCald import app
import sqlite3
from flask import render_template, Flask, redirect, request, g


app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)