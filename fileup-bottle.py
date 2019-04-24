import json;
from bottle import route, run, request, template, os,static_file, redirect;

@route('/')
def index():
    directory = os.listdir('./uploaded_files/')
    return template("Uploader.html", uploaded_files=directory)
    # return template("Uploader.html", uploaded_files=directory)


@route('/upload', method='POST')
def do_upload():
    data = request.files.get('data', '')
    if data and data.file:
        filename = data.filename
        data.save("./uploaded_files/" + filename, overwrite=True)
        redirect("/")
        return " You upload %s " %(filename)
    return "You missed a filed"

@route('/uploaded_files')
def get_uploaded_file():
    directory = os.listdir('./uploaded_files/')
    return template("Uploaded_files.html", uploaded_files=directory)

@route('/static/<file_path:path>')
def static(file_path):
    return static_file(file_path, root='./uploaded_files/', download=True)

@route("/static_files/<file_path:path>")
def host_static_files(file_path):
    return static_file(file_path, "./static_files")
    
@route("/api/uploaded_files")
def api_files():
    files = os.listdir('./uploaded_files')
    start = int(request.query.get('start', '0'))
    size = int(request.query.get('size'))
    result = {
        'files' : files[start:start+size]
    }
    return json.dumps(result)


run(host='localhost', port=8000, debug=True, reloader=True)

