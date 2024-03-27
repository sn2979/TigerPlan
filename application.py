#!/usr/bin/env python
import flask
import auth

app = flask.Flask(__name__,  template_folder='.')
app.secret_key = '12345'
#-----------------------------------------------------------------------
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    username = auth.authenticate()
    html_code = flask.render_template("/HomePage HTML/css/abani's_attempt.html", username=username)
    response = flask.make_response(html_code)
    return response

