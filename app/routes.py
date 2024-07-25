from app import app
from flask import render_template


@app.route('/')
@app.route('/Shop')
def shop():
    """Shop URL"""
    return render_template('shop.html', title='Shop')


@app.route('/')
@app.route('/Register')
def register():
    """Register URL"""
    return render_template('register.html', title='Register')


@app.route('/Login')
def login():
    """Login URL"""
    return render_template('login.html', title='login')
