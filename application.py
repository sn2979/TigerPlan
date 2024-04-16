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

def map_major_name_to_id(major):
    # Implement this function to map major_id to the corresponding major name
    # Example: This is a simplified mapping, you should replace this with your logic
    majors_mapping = {
        'African American Studies': 'AAS',
        'Anthropology': 'ANT',
        'Architecture': 'ARC',
        'Art and Archaeology': 'ART',
        'Astrophysics': 'AST',
        'Chemical and Biological Engineering': 'CBE',
        'Chemistry': 'CHM',
        'Civil and Environmental Engineering': 'CEE',
        'Classics': 'CLA',
        'Comparative Literature': 'COM',
        'Computer Science': 'COS',
        'East Asian Studies': 'EAS',
        'Economics': 'ECO',
        'Electrical and Computer Engineering': 'ECE',
        'English': 'ENG',
        'Ecology and Evolutionary Biology': 'EEB',
        'French and Italian': 'FRE',
        'Geosciences': 'GEO',
        'German': 'GER',
        'History': 'HIS',
        'Mathematics': 'MAT',
        'Mechanical and Aerospace Engineering': 'MAE',
        'Music': 'MUS',
        'Near Eastern Studies': 'NES',
        'Neuroscience': 'NEU',
        'Operations Research and Financial Engineering': 'ORF',
        'Philosophy': 'PHI',
        'Physics': 'PHY',
        'Politics': 'POL',
        'Princeton School of Public and International Affairs': 'SPI',
        'Psychology': 'PSY',
        'Religion': 'REL',
        'Slavic Languages and Literatures': 'SLA',
        'Sociology': 'SOC',
        'Spanish and Portuguese': 'SPA'
    }

    return majors_mapping.get(major, '')

def map_major_id_to_name(major):
    # Create a reverse mapping dictionary from major name to major id
    reverse_mapping = {
    'AAS': 'African American Studies',
    'ANT': 'Anthropology',
    'ARC': 'Architecture',
    'ART': 'Art and Archaeology',
    'AST': 'Astrophysics',
    'CBE': 'Chemical and Biological Engineering',
    'CHM': 'Chemistry',
    'CEE': 'Civil and Environmental Engineering',
    'CLA': 'Classics',
    'COM': 'Comparative Literature',
    'COS': 'Computer Science',
    'EAS': 'East Asian Studies',
    'ECO': 'Economics',
    'ECE': 'Electrical and Computer Engineering',
    'ENG': 'English',
    'EEB': 'Ecology and Evolutionary Biology',
    'FRE': 'French and Italian',
    'GEO': 'Geosciences',
    'GER': 'German',
    'HIS': 'History',
    'MAT': 'Mathematics',
    'MAE': 'Mechanical and Aerospace Engineering',
    'MUS': 'Music',
    'NES': 'Near Eastern Studies',
    'NEU': 'Neuroscience',
    'ORF': 'Operations Research and Financial Engineering',
    'PHI': 'Philosophy',
    'PHY': 'Physics',
    'POL': 'Politics',
    'SPI': 'Princeton School of Public and International Affairs',
    'PSY': 'Psychology',
    'REL': 'Religion',
    'SLA': 'Slavic Languages and Literatures',
    'SOC': 'Sociology',
    'SPA': 'Spanish and Portuguese'
    }

    return reverse_mapping.get(major, '')

        
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

@app.route('/profile', methods=['GET'])
def profile():
    success, username, _ = get_user_info()
    if not success:
        error_message = f"An error occurred: {str(username)}"
        return flask.render_template("error.html", error=error_message)
    name = student_database.get_student_name(username)
    major = map_major_id_to_name(student_database.get_student_major(username))
    html_code = flask.render_template("profile.html", username=username
                                      , name=name, major=major)
    response = flask.make_response(html_code)
    return response

@app.route('/update_profile', methods=['POST'])
def reset_profile():
    username = flask.session.get('username')
    if username is None:
        flask.redirect('/login')

    name = request.form.get('name')
    if name == '':
        name = student_database.get_student_name(username)

    # Retrieve the selected major id from the form data
    major_name = request.form.get('major')
    if not major_name:
        # If major_id is not provided (shouldn't happen), use default logic
        major = map_major_id_to_name(student_database.get_student_major(username))
    else:
        # update major if you get new input
        major = map_major_name_to_id(major_name)
        student_database.update_student_profile(username, name, major)

    return flask.redirect('/profile')

@app.route('/set_profile', methods=['POST'])
def set_profile():
    username = flask.session.get('username')
    if username is None:
        flask.redirect('/login')

    name = request.form.get('name')
    major = map_major_name_to_id(request.form.get('major'))
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

    html_code = flask.render_template("classboard.html", username=username, classes=classes)
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
   
    #let's do more exception handling with database on backend too later
    try:
        result = courses_database.search_courses(course) 
        if result is None: 
            result = []
        html_code = flask.render_template('course.html', courses=result)
        response = flask.make_response(html_code)
        return response
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return flask.render_template("error.html", error=error_message), 500  # Return a 500 Internal Server Error status code

@app.route('/addcourse', methods=['POST'])
def add_course():
    success, username, _ = get_user_info()
    if not success:
        error_message = f"An error occurred: {str(username)}"
        return flask.render_template("error.html", error=error_message), 500

    id = request.args.get('courseId')
    print(id)
    coursenum = request.args.get('courseNum')
    print(coursenum)
    title = request.args.get('title')
    print(title)

    course = {'id': id, 'coursenum': coursenum, 'title': title}
    try:
        student_database.update_student_classes(username, [course], None)
        return flask.redirect('/loadarea')
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return flask.render_template("error.html", error=error_message), 500



@app.route('/removecourse', methods=['POST'])
def remove_course():
    print("remove course")
    success, username, _ = get_user_info()
    if not success:
        error_message = f"An error occurred: {str(username)}"
        return flask.render_template("error.html", error=error_message), 500

    id = request.args.get('courseId')

    try:
        student_database.update_student_classes(username, classes_to_remove=[id])
        return flask.redirect('/loadarea')
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return flask.render_template("error.html", error=error_message), 500

@app.route('/loadarea', methods=['GET'])
def load_area():
    success, username, classes = get_user_info()
    if not success:
        error_message = f"An error occurred: {str(username)}"
        return flask.render_template("error.html", error=error_message), 500  # Return a 500 Internal Server Error status code

    html_code = flask.render_template("droparea.html", classes=classes)
    response = flask.make_response(html_code)
    return response