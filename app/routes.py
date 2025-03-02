from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/admin')
def admin():
    return render_template("admin.html")
