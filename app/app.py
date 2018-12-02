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

class SignupForm(Form):
    first_name = StringField('first_name', [validators.length(min = 1, max = 50)])
    last_name = StringField('last_name', [validators.length(min = 1, max = 50)])
    email = StringField('email', [validators.length(min = 4, max = 50)])
    password = PasswordField('password', [validators.DataRequired(), validators.EqualTo('confirm', message = 'Passwords do not match')])
    confirm = PasswordField('Confirm Password')
    phone = IntegerField('phone')
    organization_address = StringField('organization_address', [validators.length(min = 5, max = 100)])
    organization_name = StringField('organization_name', [validators.length(min = 1, max = 100)])
    department_name = StringField('department_name', [validators.length(min = 1, max = 100)])


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    print("HeloEntry")
    if request.method == 'POST':
        if form.validate():
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            password = sha256_crypt.encrypt(str(form.password.data))
            phone = form.phone.data
            organization_address = form.organization_address.data
            organization_name = form.organization_name.data
            department_name = form.department_name.data

            print("Helo")

            cur = mysql.connection.cursor()
            
            #Executes the SQL query
            cur.execute("INSERT INTO users(first_name, last_name, email, password, phone, organization_address, organization_name, department_name) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", (first_name, last_name, email, password, phone, organization_address, organization_name, department_name))
            mysql.connection.commit()
            cur.close()

            flash('You are now registered and can log in', 'success')

            #Redirect url after registration to login
            #redirect(url_for('login'))

            return 'success', status.HTTP_200_OK
        else:
            return "Invalid data"
    else:
        return "Invalid request method"

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


'''
@app.route('/uploader', methods=['GET', 'POST'])
def upload_file3():
    if request.method == 'POST':
        f1 = request.files['file1']
        f2 = request.files['file2']
        f1.save(secure_filename(f1.filename))
        f2.save(secure_filename(f2.filename))
        os.rename(str(f1.filename), "file1.pdf")
        os.rename(str(f2.filename), "file2.pdf")
        return getMatchedArray()
'''



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



@app.route('/uploader1', methods=['GET', 'POST'])
def upload_file1():
    if request.method == 'POST':
        f1 = request.files['file1']
        f1.save(secure_filename(f1.filename))
        os.rename(str(f1.filename), "file1.pdf")
        return render_template('match_docs.html')

@app.route('/taxonomy', methods=['GET', 'POST'])
def upload_file2():
    if request.method == 'POST':
        f2 = request.files['file2']
        f2.save(secure_filename(f2.filename))
        os.rename(str(f2.filename), "file2.pdf")
        list1,list2 = p1.createWordArray("file1.pdf","file2.pdf")
        matchedWords = p1.getMatchedWords(list1,list2)
        return render_template('matched_words.html',matchedWords=matchedWords)
        #return getMatchedArray()
        
@app.route('/dashboard',methods=['GET'])
def dashboard():
    if request.method == 'GET':
        classifiedText = cl_reg.classifyRegDoc("file2.pdf")
        return render_template('dashboard.html',classifiedText = classifiedText,count_texts=cl_reg.count_texts)


def getMatchedArray():
    matchedWords = []
    list1,list2 = p1.createWordArray("file1.pdf","file2.pdf")
    matchedWords = p1.getMatchedWords(list1,list2)
    return jsonify(matchedWords)

if __name__ == '_main_':
    app.run(debug=True)
