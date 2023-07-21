from flask import Flask, render_template, url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,Length,ValidationError
import requests
import base64
import jsonpickle


app=Flask(__name__)





@app.route('/',methods=["GET"])
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username=request.form['username']
    password=request.form['password']
    encodedUsername = base64.b64encode(username.encode())
    encodedPass = base64.b64encode(password.encode())
    fullname=""
    source=""
    client_id="client1"
    client_secret="secret"
    grant_type="password"
    url="http://konnect.quadlabs.net/CareAPI/API/Login"
    data={'username':encodedUsername,'password':encodedPass,'fullname':fullname,'source':source,'client_id':client_id,'client_secret':client_secret,'grant_type':'password'}
    obj=jsonpickle.encode(data)
    response=requests.post(url,json=obj,headers={
        'Authorization' : 'Basic Y2xpZW50MTpzZWNyZXQ='
    })

    if response.status_code==200:
        return redirect(url_for('index.html'))
    else:
        return render_template('login.html',error="Invalid username or password")

@app.route('/home')
def home():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)