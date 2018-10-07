#Höfundur: Huginn Þór Jóhannsson
from bottle import *
from sys import argv
import urllib.request, json
@error(404)
def notfound(error):
    return "404 not found D:"
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root="./static")
@route('/.css/<filepath:path>')
def css(filepath):
    return static_file(filepath,root="./.css")
@route('/')
@route('/index')
def index():
    with urllib.request.urlopen("https://apis.is/petrol")as url:
        data=json.loads(url.read().decode())
    temp=[]
    for x in data["results"]:
        if x["company"] not in temp:
            temp.append(x["company"])
    return template("forsida", data=temp, name="Heimasíða")
@route('/company')
def bensin():
    query=request.query.company
    with urllib.request.urlopen("https://apis.is/petrol")as url:
        data=json.loads(url.read().decode())
    stations=0
    for x in data["results"]:
        if x["company"] == query:
            stations+=1
    return template("bensin",data=data, name=query)
    #return "{}".format(stations)
#run(host="localhost",port=8080,reloader=True,debug=True)
run(host="0.0.0.0",port=argv[1],debug=False)
