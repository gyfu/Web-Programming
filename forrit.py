#Höfundur: Huginn Þór Jóhannsson
from bottle import *
from sys import argv
@error(404)
def error404(error):
    return "404 Not found :D"

@route('/index')
@route('/')
def index():
    return static_file('index.html', root='')

#A liður
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

@route('/myndir')
def myndir():
    mynd = request.query.mynd
    return template("<img src='{{ mynd }}'>",mynd=mynd)
    

#run(host="localhost",port=8080,debug=True,reloader=True)
run(host="0.0.0.0",port=argv[1],debug=False)
