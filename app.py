from flask import Flask, render_template, url_for
import sqlite3 
from contextodb import *

app = Flask(__name__)


#Routes

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)