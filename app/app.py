#!/usr/bin/python3
from flask import Flask, request, render_template, flash, redirect, url_for, session, logging
from werkzeug.utils import secure_filename
from flask_mysqldb import MySQL
from flask_api import status
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from wtforms_components import IntegerField
from passlib.hash import sha256_crypt

import os
#from flask_restful import Resource, Api
from flask import jsonify
import PdfToText_WordArray as p1
import classifyRegulatoryDoc as cl_reg
from flask import request

app = Flask(__name__)
app.secret_key = 'super secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'cmpe295b'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/finance')
def finance():
    classifiedText = cl_reg.classifyRegDoc("file2.pdf")
    return render_template('finance.html',classifiedText=classifiedText)

@app.route('/hr')
def hr():
    classifiedText = cl_reg.classifyRegDoc("file2.pdf")
    return render_template('HR.html',classifiedText=classifiedText)

@app.route('/marketing')
def marketing():
    classifiedText = cl_reg.classifyRegDoc("file2.pdf")
    return render_template('marketing.html',classifiedText=classifiedText)

@app.route('/purchasing')
def purchasing():
    classifiedText = cl_reg.classifyRegDoc("file2.pdf")
    return render_template('purchasing.html',classifiedText=classifiedText)


class SignupForm(Form):
    first_name = StringField('first_name', [validators.length(min = 1, max = 50)])
    last_name = StringField('last_name', [validators.length(min = 1, max = 50)])
    email = StringField('email', [validators.length(min = 1, max = 50)])
    password = PasswordField('password', [validators.DataRequired(), validators.EqualTo('confirm', message = 'Passwords do not match')])
    confirm = PasswordField('Confirm Password')
    phone = IntegerField('phone')
    organization_address = StringField('organization_address', [validators.length(min = 1, max = 100)])
    organization_name = StringField('organization_name', [validators.length(min = 1, max = 100)])


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    #print("HelloEntry")

    print(form.first_name.data)
    print(form.last_name.data)
    print(form.email.data)
    print(form.password.data)
    print(form.phone.data)
    print(form.organization_address.data)
    print(form.organization_name.data)
    print(form.first_name.data)

    if request.method == 'GET':
            return render_template('./signup_manager.html')

    if request.method == 'POST':
        if form.validate():
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            password = sha256_crypt.encrypt(str(form.password.data))
            phone = form.phone.data
            organization_address = form.organization_address.data
            organization_name = form.organization_name.data

        #print("Hello")

            cur = mysql.connection.cursor()
            
            #Executes the SQL query
            cur.execute("INSERT INTO users(first_name, last_name, email, password, phone, organization_address, organization_name) VALUES(%s, %s, %s, %s, %s, %s, %s)", (first_name, last_name, email, password, phone, organization_address, organization_name))
            mysql.connection.commit()
            cur.close()

            flash('You are now registered and can log in', 'success')

            #Redirect url after registration to login
            #redirect(url_for('login'))

            return redirect(url_for('home'))
        else:
            return "Invalid data"
    else:
        return "Invalid request method"


@app.route('/login', methods=['GET', 'POST'])
def login():
    print("HelloEntry")
    print(request.method)

    print(session.get('email'))
    if request.method == "GET":
        if(session.get('logged_in')):
            if(session['logged_in']==True):
                return redirect(url_for('upload_files'))
        else: 
            return render_template('login.html' )

    if request.method == "POST":
        print("here")
        print(request.form['email'])
        print("here2")
        email = request.form['email']
        print("here3")
        password_user = request.form['password_user']
        print("here4")

        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM users WHERE email = %s", [email])
        print(result)

        print("Hello")

        if(result > 0):
            data = cur.fetchone()
            password = data['password']

            if sha256_crypt.verify(password_user, password):
                app.logger.info('PASSWORD MATCHED')
                
                session['logged_in'] = True
                session['email'] = email
                return redirect(url_for('upload_files'))
            else:
                error = "Invalid login."
                app.logger.info('PASSWORD IS INCORRECT')
                return "Invalid login", status.HTTP_401_UNAUTHORIZED

        else:
            error = "Username not found"
            return render_template('login.html', error=error)
        cur.close()

    return redirect(url_for('upload_files')), status.HTTP_200_OK


@app.route('/logout', methods=['POST','GET'])
def logout():
        if (request.method == "GET"):
            if(session.get('logged_in')):
                session.clear()
                flash('You are now logged out', 'success')
                return "Success! You are now logged out", status.HTTP_200_OK

            else:
                return render_template('login.html' )

@app.route('/uploaderabhi', methods=['POST'])
def formdata():
        print(request.form['firstname'])
        print(request.form['lastname'])
        print(request.form['email'])
        #print(request.form['email'])
        return "Done"

   


@app.route('/matchdocs')
def match_docs():
    return render_template('match_docs.html')

@app.route('/about')
def about():
    return render_template('./about/about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/team')
def team():
    return render_template('team.html')

# prevent cached responses
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r



@app.route('/upload', methods=['GET', 'POST'])
def upload_files():
        return render_template('match_docs.html')

@app.route('/taxonomy', methods=['GET', 'POST'])
def word_matching():
    if request.method == 'POST':
        f1 = request.files['file1']
        f2 = request.files['file2']
        f1.save(secure_filename(f1.filename))
        f2.save(secure_filename(f2.filename))
        os.rename(str(f1.filename), "file1.pdf")
        os.rename(str(f2.filename), "file2.pdf")
        list1,list2 = p1.createWordArray("file1.pdf","file2.pdf")
        matchedWords = p1.getMatchedWords(list1,list2)
        return render_template('matched_words.html',matchedWords=matchedWords)
        #return getMatchedArray()
        
@app.route('/dashboard',methods=['GET'])
def dashboard():
    if request.method == 'GET':
        return render_template('dashboard.html')


def getMatchedArray():
    matchedWords = []
    list1,list2 = p1.createWordArray("file1.pdf","file2.pdf")
    matchedWords = p1.getMatchedWords(list1,list2)
    return jsonify(matchedWords)


if __name__ == '_main_':
    app.run(debug=True)
