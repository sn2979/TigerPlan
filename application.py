#!/usr/bin/env python
import flask 
from flask import request
import database_files.student_database as student_database
import database_files.courses_database as courses_database
import database_files.minors_database as minors_database
import json

import dotenv
import auth
import recommendation
import courses as course_dicts
import recommender2
import math

app = flask.Flask(__name__,  template_folder='templates')
app.secret_key = '12345'

'''
unsure what these mean, were in ref prog
dotenv.load_dotenv()
app.secret_key = os.environ['APP_SECRET_KEY']

'''
def login_required(previous_page_url):
        flask.session['previous_page'] = previous_page_url
        return flask.redirect('/login')

#-----------------------------------------------------------------------
def restricted_access(func):
    def wrapper(*args, **kwargs):
        # Check if the request comes from a form submission
        if flask.request.referrer is None:
            # If not, redirect the user to the error page
            return flask.redirect('/error')
        # If the request comes from a form submission, proceed to the original function
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper
#-----------------------------------------------------------------------

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    try:
        username = flask.session.get('username')
        html_code = flask.render_template("homepage.html", username=username)
        response = flask.make_response(html_code)
        return response
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return flask.render_template("error.html", username=flask.session.get('username'), error=error_message), 500

#-----------------------------------------------------------------------
#username and classes retrieval 
def get_user_info():
    # Retrieve the username from the session
    username = flask.session.get('username')
    if username is None:
        # Handle case where username is not in session (e.g., user not logged in)
        return False, None, []  # Redirect to login page
    
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
        'African Studies': 'AFS',
        'Asian American Studies': 'ASA',
        'Anthropology': 'ANT',
        'Architecture': 'ARC',
        'Art and Archaeology': 'ART',
        'Astrophysics': 'AST',
        'Chemical and Biological Engineering': 'CBE',
        'Chemistry': 'CHM',
        'Chinese Language': 'CHI',
        'Civil and Environmental Engineering': 'CEE',
        'Classics': 'CLA',
        'Climate Science': 'CS',
        'Comparative Literature': 'COM',
        'Computer Science': 'COS',
        'Creative Writing': 'CWR',
        'Dance': 'DAN',
        'East Asian Studies': 'EAS',
        'Economics': 'ECO',
        'Electrical and Computer Engineering': 'ECE',
        'English': 'ENG',
        'Environmental Studies': 'ENV',
        'Ecology and Evolutionary Biology': 'EEB',
        'Finance': 'FIN',
        'French and Italian': 'FRE',
        'Geosciences': 'GEO',
        'German': 'GER',
        'Global Health and Health Policy': 'GHP',
        'Gender Sexuality Studies': 'GSS',
        'History': 'HIS',
        'Hellenic Studies': 'HLS',
        'History of Science, Technology, and Medicine': 'HSTM',
        'Humanistic Studies': 'HUM',
        'Japanese Language': 'JPN',
        'Journalism': 'JRN',
        'Korean Language': 'KOR',
        'Latino Studies': 'LAO',
        'Linguistics': 'LIN',
        'Mathematics': 'MAT',
        'Materials Science and Engineering': 'MSE',
        'Mechanical and Aerospace Engineering': 'MAE',
        'Medieval Studies': 'MED',
        'Music': 'MUS',
        'Music Performance': 'MPP',
        'Near Eastern Studies': 'NES',
        'Neuroscience': 'NEU',
        'Operations Research and Financial Engineering': 'ORF',
        'Translation and Intercultural Communication': 'TRA',
        'Philosophy': 'PHI',
        'Physics': 'PHY',
        'Politics': 'POL',
        'Princeton School of Public and International Affairs': 'SPI',
        'Psychology': 'PSY',
        'Quantitative Economics': 'MQE',
        'Quantitative and Computational Biology': 'QCB',
        'Russian, East European, and Eurasian Studies': 'RES',
        'Religion': 'REL',
        'Souh Asian Studies': 'SAS',
        'Slavic Languages and Literatures': 'SLA',
        'Statistics and Machine Learning': 'SML',
        'Sociology': 'SOC',
        'Spanish and Portuguese': 'SPA',
        'Theater and Music Theater': 'TMT',
        'Visual Arts': 'VIS',
        'Values and Public Life': 'VPL'
    }

    return majors_mapping.get(major, '')

def map_major_id_to_name(major):
    # Create a reverse mapping dictionary from major name to major id
    reverse_mapping = {
    'AAS': 'African American Studies',
    'AFS': 'African Studies',
    'ASA': 'Asian American Studies',
    'ANT': 'Anthropology',
    'ARC': 'Architecture',
    'ART': 'Art and Archaeology',
    'AST': 'Astrophysics',
    'CBE': 'Chemical and Biological Engineering',
    'CHM': 'Chemistry',
    'CHI': 'Chinese Language',
    'CEE': 'Civil and Environmental Engineering',
    'CLA': 'Classics',
    'CS': 'Climate Science',
    'COM': 'Comparative Literature',
    'COS': 'Computer Science',
    'CWR': 'Creative Writing',
    'DAN': 'Dance',
    'EAS': 'East Asian Studies',
    'ECO': 'Economics',
    'ECE': 'Electrical and Computer Engineering',
    'ENG': 'English',
    'ENV': 'Environmental Studies',
    'EEB': 'Ecology and Evolutionary Biology',
    'FIN': 'Finance',
    'FRE': 'French and Italian',
    'GEO': 'Geosciences',
    'GER': 'German',
    'GHP': 'Global Health and Health Policy',
    'GSS': 'Gender Sexuality Studies',
    'HIS': 'History',
    'HLS': 'Hellenic Studies',
    'HSTM': 'History of Science, Technology, and Medicine',
    'HUM': 'Humanistic Studies',
    'JPN': 'Japanese Language',
    'JRN': 'Journalism',
    'KOR': 'Korean Language',
    'LAO': 'Latino Studies',
    'LIN': 'Linguistics',
    'MAT': 'Mathematics',
    'MSE': 'Materials Science and Engineering',
    'MAE': 'Mechanical and Aerospace Engineering',
    'MED': 'Medieval Studies',
    'MUS': 'Music',
    'MPP': 'Music Performance',
    'NES': 'Near Eastern Studies',
    'NEU': 'Neuroscience',
    'ORF': 'Operations Research and Financial Engineering',
    'TRA': 'Translation and Intercultural Communication',
    'PHI': 'Philosophy',
    'PHY': 'Physics',
    'POL': 'Politics',
    'SPI': 'Princeton School of Public and International Affairs',
    'PSY': 'Psychology',
    'MQE': 'Quantitative Economics',
    'QCB': 'Quantitative and Computational Biology',
    'RES': 'Russian, East European, and Eurasian Studies',
    'REL': 'Religion',
    'SAS': 'South Asian Studies',
    'SLA': 'Slavic Languages and Literatures',
    'SML': 'Statistics and Machine Learning',
    'SOC': 'Sociology',
    'SPA': 'Spanish and Portuguese',
    'TMT': 'Theater and Music Theater',
    'VIS': 'Visual Arts',
    'VPL': 'Values and Public Life'
}


    return reverse_mapping.get(major, '')

def generate_and_store_recommendations(username):
    try:
    # Placeholder recommendation logic
        courses = student_database.get_student_coursenums(username)
        recommended_courses = list(recommendation.recommend(courses, username))
        print("recommended!")

        # Store recommended courses in the database
        student_database.store_recommendations(username, recommended_courses)
        print("stored!")

        return recommended_courses
    except Exception as e:
        raise e

def distance_to_minor(username, class_list, minor):
    try:
        courses = recommendation.categorize_courses(class_list, course_dicts.get_courses(minor))
        subrequirements = course_dicts.get_minor_requirements(minor)

        _, combinations = recommender2.generate_combinations(courses, subrequirements)
        if len(combinations) == 0:
            best_combination = []
            tree_description = ''
            distance = math.inf
        else:
            best_combination, _, classes_taken_needed, _, tree_description = recommender2.find_best_combination(minor, combinations, subrequirements)
            distance = classes_taken_needed[1] - classes_taken_needed[0]

        course =  {'distance': distance, 'minor': minor, 'best_combination': best_combination, 'tree_description': tree_description}

        return course
    except Exception as e:
        raise e
    
        
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
            if flask.session.get('previous_page') == None:
                return flask.redirect('/classboard')
            else:
                return flask.redirect(flask.session['previous_page']) 
    else:
        # Handle authentication failure
        return flask.abort(401)  # Unauthorized

@app.route('/logoutapp', methods=['GET'])
def logoutapp():
    flask.session.pop('username', None)  # Remove username from session
    return auth.logoutapp()

@app.route('/logoutcas', methods=['GET'])
def logoutcas():
    flask.session.pop('username', None)  # Remove username from session
    return auth.logoutcas()

#-----------------------------------------------------------------------
#Routes for profile. 

@app.route('/profile', methods=['GET'])
def profile():
    try:
        success, username, _ = get_user_info()
        if username is None:
            return login_required(previous_page_url='/profile')
        if not success:
            error_message = f"An error occurred: {str(username)}"
            return flask.render_template("error.html", username=flask.session.get('username'), error=error_message)
        name = student_database.get_student_name(username)
        major = map_major_id_to_name(student_database.get_student_major(username))
        html_code = flask.render_template("profile.html", username=username
                                        , name=name, major=major)
        response = flask.make_response(html_code)
        return response
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return flask.render_template("error.html", username=flask.session.get('username'), error=error_message), 500

@app.route('/update_profile', methods=['POST'])
@restricted_access
def reset_profile():
    try:
        username = flask.session.get('username')
        if username is None:
            return login_required(previous_page_url='/update_profile')

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
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return flask.render_template("error.html", username=flask.session.get('username'), error=error_message), 500

@app.route('/set_profile', methods=['POST'])
def set_profile():
    try:
        username = flask.session.get('username')
        if username is None:
            return flask.redirect('/login')

        name = request.form.get('name')
        major = map_major_name_to_id(request.form.get('major'))
        student_database.update_student_profile(username, name, major)
        return flask.redirect('/classboard')
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return flask.render_template("error.html", username=flask.session.get('username'), error=error_message), 500

#-----------------------------------------------------------------------
# Routes for All Minors page
@app.route('/allminors', methods=['GET'])
def allminors():
    try:
        success, username, _ = get_user_info()
        if username is None:
            return login_required(previous_page_url='/allminors')
        if not success:
            error_message = f"An error occurred: {str(username)}"
            return flask.render_template("error.html", username=flask.session.get('username'), error=error_message), 500
        
        minors = minors_database.get_all_minors()
        html_code = flask.render_template("allminors.html", username=username, minors=minors)
        response = flask.make_response(html_code)
        return response
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return flask.render_template("error.html", username=flask.session.get('username'), error=error_message), 500
    
@app.route('/distance', methods=['GET'])
def minor():
    try:
        success, username, _ = get_user_info()
        if username is None:
            return login_required(previous_page_url='/minor')
        if not success:
            error_message = f"An error occurred: {str(username)}"
            return flask.render_template("error.html", username=flask.session.get('username'), error=error_message), 500
        
        # find the distance to the clicked on minor
        minor_code = request.args.get('code')
        print(minor_code)

        # recommendation logic using recommender2
        class_list = student_database.get_student_coursenums(username)

        recommendation = distance_to_minor(username, class_list, minor_code)


        recommendation['minorid'] = recommendation['minor']
        recommendation['minor'] = map_major_id_to_name(recommendation['minor'])
        #reminder to self to add truncation of description if too long
        recommendation['desc'] = minors_database.get_desc(recommendation['minorid'])
        recommendation['urls'] = minors_database.get_urls(recommendation['minorid'])

        return flask.render_template("minor.html", username=username, course=recommendation)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return flask.render_template("error.html", username=flask.session.get('username'), error=error_message), 500

#-----------------------------------------------------------------------
#Routes for classboard. 

@app.route('/classboard', methods=['GET'])
def classboard():
    try:
        success, username, classes = get_user_info()
        if username is None:
            return login_required(previous_page_url='/classboard')
        if not success:
            error_message = f"An error occurred: {str(username)}"
            return flask.render_template("error.html", username=flask.session.get('username'), error=error_message), 500  # Return a 500 Internal Server Error status code

        html_code = flask.render_template("classboard.html", username=username, classes=classes)
        response = flask.make_response(html_code)
        return response
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return flask.render_template("error.html", username=flask.session.get('username'), error=error_message), 500

@app.route('/searchresults', methods=['GET'])
@restricted_access
def search_results():
    try:
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
            return flask.render_template("error.html", username=flask.session.get('username'), error=error_message), 500  # Return a 500 Internal Server Error status code
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return flask.render_template("error.html", username=flask.session.get('username'), error=error_message), 500

@app.route('/addcourse', methods=['POST'])
def add_course():
    try:
        success, username, _ = get_user_info()
        if username is None:
            return login_required(previous_page_url='/addcourse')
        if not success:
            error_message = f"An error occurred: {str(username)}"
            return flask.render_template("error.html", username=flask.session.get('username'), error=error_message), 500

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
            return flask.render_template("error.html", username=flask.session.get('username'), error=error_message), 500
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return flask.render_template("error.html", username=flask.session.get('username'), error=error_message), 500

@app.route('/removecourse', methods=['POST'])
def remove_course():
    try:
        print("remove course")
        success, username, _ = get_user_info()
        if username is None:
            return login_required(previous_page_url='/removecourse')
        if not success:
            error_message = f"An error occurred: {str(username)}"
            return flask.render_template("error.html", username=flask.session.get('username'), error=error_message), 500

        id = request.args.get('courseId')

        try:
            student_database.update_student_classes(username, classes_to_remove=[id])
            return flask.redirect('/loadarea')
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return flask.render_template("error.html", username=flask.session.get('username'), error=error_message), 500
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return flask.render_template("error.html", username=flask.session.get('username'), error=error_message), 500
    
@app.route('/loadarea', methods=['GET'])
@restricted_access
def load_area():
    try:
        success, username, classes = get_user_info()
        if username is None:
            return login_required(previous_page_url='/loadarea')
        if not success:
            error_message = f"An error occurred: {str(username)}"
            return flask.render_template("error.html", username=flask.session.get('username'), error=error_message), 500  # Return a 500 Internal Server Error status code

        html_code = flask.render_template("droparea.html", classes=classes)
        response = flask.make_response(html_code)
        return response
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return flask.render_template("error.html", username=flask.session.get('username'), error=error_message), 500


#-----------------------------------------------------------------------
#Routes for recommend. 

@app.route('/recommend', methods=['GET'])
def recommend():
    try:
        success, username, classes = get_user_info()
        if username is None:
            return login_required(previous_page_url='/recommend')
        if not success:
            error_message = f"An error occurred: {str(username)}"
            return flask.render_template("error.html", username=flask.session.get('username'), error=error_message), 500
        
        _ = generate_and_store_recommendations(username)
        # reroute to recommendations page
        return flask.redirect('/recommendations')
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return flask.render_template("error.html", username=flask.session.get('username'), error=error_message), 500

@app.route('/recommendations', methods=['GET'])
def recommendations():
    try:
        success, username, classes = get_user_info()
        if username is None:
            return login_required(previous_page_url='/recommendations')
        if not success:
            error_message = f"An error occurred: {str(username)}"
            return flask.render_template("error.html", username=flask.session.get('username'), error=error_message), 500
        
        stored_recommendations = student_database.get_stored_recommendations(username)

        if not stored_recommendations:
            # No stored recommendations found, generate and store new ones
            stored_recommendations = generate_and_store_recommendations(username)

        # Map minor IDs to names for display
        for course in stored_recommendations:
            course['minorid'] = course['minor']
            course['minor'] = map_major_id_to_name(course['minor'])
            #reminder to self to add truncation of description if too long
            course['desc'] = minors_database.get_desc(course['minorid'])
            course['urls'] = minors_database.get_urls(course['minorid'])

            #course['tree_description'] = json.loads(course['tree_description'])

        return flask.render_template("recommend.html", username=username, courses=stored_recommendations)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return flask.render_template("error.html", username=flask.session.get('username'), error=error_message), 500
    
@app.errorhandler(405)
def access_not_allowed(e):
    return flask.render_template('error.html', username=flask.session.get('username'), error="You do not have access to this page"), 405

@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('error.html', username=flask.session.get('username'), error="The requested page does not exist"), 404

@app.route('/details', methods = ['GET'])
@restricted_access
def details():
    try:
        success, username, _ = get_user_info()
        if username is None:
            return login_required(previous_page_url='/details')
        if not success:
            error_message = f"An error occurred: {str(username)}"
            return flask.render_template("error.html", username=flask.session.get('username'), error=error_message), 500  # Return a 500 Internal Server Error status code

        minor = flask.request.args.get('minor')
        # print(minor)
        return flask.render_template("minor.html", username=username, minor = minor)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return flask.render_template("error.html", username=flask.session.get('username'), error=error_message), 500


#-----------------------------------------------------------------------
#Other routes

@app.route('/about', methods=['GET'])
def about():
    try:
        success, username, _ = get_user_info()
        if username is None:
            return login_required(previous_page_url='/about')
        if not success:
            error_message = f"An error occurred: {str(username)}"
            return flask.render_template("error.html", username=flask.session.get('username'), error=error_message), 500  # Return a 500 Internal Server Error status code

        html_code = flask.render_template("about.html", username = username)
        response = flask.make_response(html_code)
        return response
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return flask.render_template("error.html", username=flask.session.get('username'), error=error_message), 500


#route to a testing page; delete later
# @app.route('/test', methods=['GET'])
# def test():
#     success, username, _ = get_user_info()
#     if username is None:
#         return login_required(previous_page_url='/test')
#     if not success:
#         error_message = f"An error occurred: {str(username)}"
#         return flask.render_template("error.html", error=error_message), 500  # Return a 500 Internal Server Error status code

#     html_code = flask.render_template("tester.html", username = username)
#     response = flask.make_response(html_code)
#     return response