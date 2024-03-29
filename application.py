#!/usr/bin/env python
import flask 
from flask import request
from student_database import handle_student_login, get_student_classes
import dotenv
import auth

app = flask.Flask(__name__,  template_folder='templates')
app.secret_key = '12345'

'''
unsure what these mean, were in ref prog
dotenv.load_dotenv()
app.secret_key = os.environ['APP_SECRET_KEY']

'''

#-----------------------------------------------------------------------
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    html_code = flask.render_template("abani's_attempt.html")
    response = flask.make_response(html_code)
    return response

#-----------------------------------------------------------------------
#Routes for authentication. 

@app.route('/login', methods=['GET'])
def login():
    username = auth.authenticate()
    html_code = flask.render_template("loginpage.html", username = username)

    response = flask.make_response(html_code)
    return response
    

@app.route('/logoutapp', methods=['GET'])
def logoutapp():
    return auth.logoutapp()

@app.route('/logoutcas', methods=['GET'])
def logoutcas():
    return auth.logoutcas()

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    name = request.form['name']
    major = request.form['major']
    
    success, first_time = handle_student_login(username,name,major)
    classes = get_student_classes(username)
    if success:
        print("inserted into database")
        html_code = flask.render_template("figma_classboard.html", username = username, classes = classes)
        response = flask.make_response(html_code)
        return response
    else:
        #fix this later w a real error screen
        html_code = flask.render_template("figma_classboard.html", username = "error")
        response = flask.make_response(html_code)
        return response

