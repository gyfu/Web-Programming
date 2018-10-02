#Höfundur: Huginn Þór Jóhannsson
from bottle import *
from sys import argv
@error(404)
def error404(error):
    return "404 Not found"
#A liður
@route('/')
def index():
    return "Main index page"

#B liður

#run(host="localhost",port=8080,debug=True)
run(host="0.0.0.0",port=argv[1],debug=False)
