#!/usr/bin/env python
import flask 
from flask import request
import database_files.student_database as student_database
import database_files.courses_database as courses_database
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
    html_code = flask.render_template("homepage.html")
    response = flask.make_response(html_code)
    return response

#-----------------------------------------------------------------------
#username and classes retrieval 
def get_user_info():
     # Retrieve the username from the session
    username = flask.session.get('username')
    if username is None:
        # Handle case where username is not in session (e.g., user not logged in)
        return flask.redirect('/login')  # Unauthorized
    
    try:
        # Retrieve other data using the username from the session
        classes = student_database.get_student_classes(username)
        name = student_database.get_student_name(username)
        if name == '': 
            name = username
        return True, username, classes
    except Exception as e:
        # Handle database retrieval or rendering errors
        return False, e, []
        
#-----------------------------------------------------------------------
#Routes for authentication. 

@app.route('/login', methods=['GET'])
def login():
    username = auth.authenticate()
    success, first_time = student_database.handle_student_login(username)
    if success:
        # Store the username in the session
        flask.session['username'] = username
        
        if first_time:
            print("First time login")
            html_code = flask.render_template("loginpage.html", username=username)
            response = flask.make_response(html_code)
            return response
        else:
            print("Returning user")
            return flask.redirect('/classboard') 
    else:
        # Handle authentication failure
        return flask.abort(401)  # Unauthorized

@app.route('/profile', methods=['POST'])
def set_profile():
    username = flask.session.get('username')
    if username is None:
        flask.redirect('/login')
    name = request.form.get('name')
    major = request.form.get('major')
    student_database.update_student_profile(username, name, major)
    return flask.redirect('/classboard')

@app.route('/logoutapp', methods=['GET'])
def logoutapp():
    flask.session.pop('username', None)  # Remove username from session
    return auth.logoutapp()

@app.route('/logoutcas', methods=['GET'])
def logoutcas():
    flask.session.pop('username', None)  # Remove username from session
    return auth.logoutcas()

@app.route('/classboard', methods=['GET'])
def classboard():
    success, username, classes = get_user_info()
    if not success:
        error_message = f"An error occurred: {str(username)}"
        return flask.render_template("error.html", error=error_message), 500  # Return a 500 Internal Server Error status code

    html_code = flask.render_template("classboard.html", username = username, classes = classes)
    response = flask.make_response(html_code)
    return response
    

@app.route('/recommend', methods=['GET'])
def recommend():
    success, username, _ = get_user_info()
    if not success:
        error_message = f"An error occurred: {str(username)}"
        return flask.render_template("error.html", error=error_message), 500  # Return a 500 Internal Server Error status code

    
    html_code = flask.render_template("recommend.html", username = username)
    response = flask.make_response(html_code)
    return response 

@app.route('/about', methods=['GET'])
def about():
    success, username, _ = get_user_info()
    if not success:
        error_message = f"An error occurred: {str(username)}"
        return flask.render_template("error.html", error=error_message), 500  # Return a 500 Internal Server Error status code

    html_code = flask.render_template("about.html", username = username)
    response = flask.make_response(html_code)
    return response



#route to a testing page; delete later
@app.route('/test', methods=['GET'])
def test():
    success, username, _ = get_user_info()
    if not success:
        error_message = f"An error occurred: {str(username)}"
        return flask.render_template("error.html", error=error_message), 500  # Return a 500 Internal Server Error status code

    html_code = flask.render_template("tester.html", username = username)
    response = flask.make_response(html_code)
    return response

@app.route('/searchresults', methods=['GET'])
def search_results():
    
    course = flask.request.args.get('course')
    if course is None:
        course = ''
    course = course.strip()

    if course == '':
        result = []
    else:
        #let's do more exception handling with database on backend too later
        try:
            result = courses_database.search_courses(course) 
            print(result[0])
            html_code = flask.render_template('course.html', courses=result)
            response = flask.make_response(html_code)
            return response
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return flask.render_template("error.html", error=error_message), 500  # Return a 500 Internal Server Error status code

