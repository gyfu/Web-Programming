#Höfundur: Huginn Þór Jóhannsson
from bottle import *
from sys import argv
@error(404)
def error404(error):
    return "404 Not found"
#A liður
@route('/index')
def index():
    return static_file("index.html",root="./index.html")
@route('/myndir/<mynd>')
def mynd(mynd):
    return mynd

#run(host="localhost",port=8080,debug=True)
run(host="0.0.0.0",port=argv[1],debug=False)
