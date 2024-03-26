#!/usr/bin/env python
import flask
import authenticate

app = flask.Flask(__name__,  template_folder='.')

#-----------------------------------------------------------------------
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    username = authenticate.authenticate()
    html_code = flask.render_template("/HomePage HTML/css/abani's_attempt.html", username=username)
    response = flask.make_response(html_code)
    return response

