from flask import Flask, render_template, url_for,request,redirect,g,session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin,LoginManager
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,Length,ValidationError
import requests
import base64
import jsonpickle
import pandas as pd
import numpy as np
import sqlite3
from models import insertToken

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
app.config['SECRET_KEY']='thisisasecretkey'
db=SQLAlchemy(app)
app.app_context().push()
conn = sqlite3.connect('database.db')


class AccessToken(db.Model):
    id=db.Column(db.Integer, primary_key=True,)
    token=db.Column(db.String(255),nullable=False)

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
    client_secret="s11ecret"
    grant_type="password"
    url="http://konnect.quadlabs.net/CareAPI/API/Login"
    data={'username':encodedUsername,'password':encodedPass,'fullname':fullname,'source':source,'client_id':client_id,'client_secret':client_secret,'grant_type':'password'}
    obj=jsonpickle.encode(data)
    response=requests.post(url,data=data,headers={
        'Authorization' : 'Basic Y2xpZW50MTpzZWNyZXQ='
    })

    if response.status_code==200:
        respData = jsonpickle.decode(response.content)

        print(respData['access_token'])
        insertToken(respData['access_token'])
        session['response']=respData['access_token']

        return redirect('/home')
    else:
        return render_template('login.html',error="Invalid username or password")

@app.route('/home')
def home():
    if 'response' in session:
        s=session['response']
        return render_template('index.html')
    return redirect('/login')

@app.route('/email',methods=['GET','POST'])
def email():
    if 'response' in session:
        s=session['response']
        return render_template('email.html')
    return redirect('/login')

    

if __name__=='__main__':
    app.run(debug=True)