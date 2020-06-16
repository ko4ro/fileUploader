# -*- coding: utf-8 -*-

import json
import os
import argparse
from bottle import Bottle, run, request, template, static_file, redirect

# from api import api

app = Bottle()
STATIC_FILES_DIR = './static_files'


@app.route('/')
def index():
    directory = get_save_path()
    return template("Uploader.html", uploaded_files=directory)


def get_save_path():
    path_dir = "./uploaded_files/"
    if not os.path.exists(path_dir):
        os.mkdir(path_dir)
    return path_dir

# Download
@app.route('/static/<file_path:path>')
def static(file_path):
    return static_file(file_path, root='./uploaded_files/', download=True)


@app.route("/static_img/<img_filepath:path>")
def static_img(img_filepath):
    return static_file(img_filepath, root='./uploaded_files/')


@app.route("/static_files/<file_path:path>")
def host_static_files(file_path):
    return static_file(file_path, STATIC_FILES_DIR)


@app.route('/upload', method='POST')
def do_upload():
    data = request.files.get('data', '')
    if data and data.file:
        print(data.filename)
        filename = data.filename
        data.save(get_save_path() + filename, overwrite=True)
        redirect("/")
        return " You upload %s " % (filename)
    return "You missed a filed"


# アップロード一覧　/uploaded_files
@app.route('/uploaded_files')
def get_uploaded_file():
    directory = os.listdir('./uploaded_files/')
    return template("Uploaded_files.html", uploaded_files=directory)


@app.route("/api/delete")
def do_delete():
    target = request.query.get('target')
    file_path = os.path.join(os.path.abspath('./uploaded_files'),target)
    try:
        os.remove(os.path.abspath(file_path))
    except FileNotFoundError:
        print("FileNotFoundError")
    return 0


@app.route("/api/uploaded_files")
def api_files():
    files = os.listdir('./uploaded_files')
    start = int(request.query.get('start', '0'))
    size = int(request.query.get('size'))
    result = {
        'files': files[start: start + size]
    }
    return json.dumps(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, default='localhost')
    parser.add_argument('--port', type=int, default=8000)

    args = parser.parse_args()
    run(app=app, host=args.host, port=args.port, debug=True, reloader=True)


if __name__ == '__main__':
    main()
