import render
import json
from functools import update_wrapper
from datetime import timedelta
from flask import Flask, request, session, g, jsonify, \
    redirect, url_for, abort, render_template, flash, \
    send_from_directory, current_app, make_response

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)

def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    """http://flask.pocoo.org/snippets/56/"""
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator
 

@app.route('/render', methods=['GET'])
@crossdomain(origin='*')
def render_image():
    #options = request.values['options']
    #render.get_kinome_layer()
    resp = send_from_directory('static', 'kinome.png', as_attachment=True)
    render.render_kinome(request.values['svg'])
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
