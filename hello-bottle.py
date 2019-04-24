# confing:utf-8

from bottle import route, run, template,post,request;

@route('/')
def main():
    return template("Post.html", test="hello")

@route('/post', method='POST')
def post():
    username = request.forms.get('username')
    return "POST IS {username}".format(username=username)

@route('/uploaded')
def main():
    return template("Post.html")

run(host='localhost', port=8000, debug=True)

