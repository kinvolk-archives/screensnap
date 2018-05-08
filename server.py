#!/usr/bin/env python3

import os
import uuid

from flask import Flask, render_template, request, redirect, abort, send_file
from dotenv import load_dotenv
from screensnap_celery_app import screenshot_task
from screensnap_storage import get

load_dotenv(verbose=True)

app = Flask(__name__)
app.secret_key = 'insecure'


@app.route('/screenshots/<screenshot_id>', methods=['GET'])
def screenshots(screenshot_id):
    image_data = get('{}.png'.format(screenshot_id))
    if not image_data:
        abort(404)
    return send_file(image_data, mimetype='image/png')


@app.route('/screenshots', methods=['POST'])
def screenshots_post():
    url = request.form['url']
    if url == "":
        abort(400)
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://{}'.format(url)
    screenshot_id = str(uuid.uuid4())
    screenshot_task.delay(url, screenshot_id)
    return redirect('/screenshot?id={}'.format(screenshot_id))


@app.route('/screenshot', methods=['GET'])
def screenshot():
    return render_template('screenshot.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    host = os.getenv('SCREENSNAP_HOST', '0.0.0.0')
    port = os.getenv('SCREENSNAP_PORT', 5000)
    app.run(host=host, port=port, debug=True)
