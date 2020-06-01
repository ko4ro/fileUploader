# -*- coding: utf-8 -*-

import json
import os
from bottle import route, run, request, template, static_file, redirect


@route('/')
def index():
    directory = get_save_path()
    return template("Uploader.html", uploaded_files=directory)


def get_save_path():
    path_dir = "./uploaded_files/"
    if not os.path.exists(path_dir):
        os.mkdir(path_dir)
    return path_dir

# Download
@route('/static/<file_path:path>')
def static(file_path):
    return static_file(file_path, root='./uploaded_files/', download=True)


@route('/sample_image.png')
def sample_image():
    return static_file('./uploaded_files/test.png', root='.')


# @route("/static_files/<file_path:path>")
# def host_static_files(file_path):
#     return static_file(file_path, "./static_files")


@route('/upload', method='POST')
def do_upload():
    data = request.files.get('data', '')
    if data and data.file:
        filename = data.filename
        data.save(get_save_path() + filename, overwrite=True)
        redirect("/")
        return " You upload %s " % (filename)
    return "You missed a filed"


# アップロード一覧　/uploaded_files
# @route('/uploaded_files')
# def get_uploaded_file():
#     directory = os.listdir('./uploaded_files/')
#     return template("Uploaded_files.html", uploaded_files=directory)


@route("/api/uploaded_files")
def api_files():
    files = os.listdir('./uploaded_files')
    start = int(request.query.get('start', '0'))
    size = int(request.query.get('size'))
    result = {
        'files': files[start: start + size]
    }
    return json.dumps(result)


if __name__ == "__main__":
    run(host='localhost', port=8000, debug=True, reloader=True)
